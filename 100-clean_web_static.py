#!/usr/bin/python3
"""
Title: Keep it clean (Fabric)
Description: Fabric script (based on the file 3-deploy_web_static.py)
            that deletes out-of-date archives, using the function do_clean:
Author: a_idk
"""

from fabric.api import *
# from fabric.api import local
# from fabric.api import put
# from fabric.api import run
import os
# from datetime import datetime

env.hosts = ['54.175.115.175', '54.237.55.177']  # my web servers


def do_clean(number=0):
    """
    Method that deletes outdated archives
    """
    if int(number) == 0:
        number = 1
    else:
        int(number)
    # 1: compress the repo to make a tgz archive
    try:
        dt = datetime.now().strftime("%Y%m%d%H%M%S")

        if os.path.isdir("versions") is False:
            local("mkdir versions")

        f_name = f'versions/web_static_{dt}.tgz'
        local(f'tar -cvzf {f_name} web_static')
        return f_name
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Method that distributes an archive to my web servers
    """
    # check if path exist
    if os.path.exists(archive_path) is False:
        return False

    try:
        d_file = archive_path.split("/")[-1]
        f_name = d_file.split(".")[0]
        f_path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run(f'mkdir -p {f_path}{f_name}/')
        run(f'tar -xzf /tmp/{d_file} -C {f_path}{f_name}/')
        run(f'rm /tmp/{d_file}')
        run('mv {0}{1}/web_static/* {0}{1}/'.format(f_path, f_name))
        run(f'rm -rf {f_path}{f_name}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {f_path}{f_name}/ /data/web_static/current')
        return True
    except Exception as e:
        return False

def deploy():
    """
    Method that deploys the archive to the web servers
    """
    arch_dir = do_pack()

    if arch_dir is None:
        return False
    return do_deploy(arch_dir)
