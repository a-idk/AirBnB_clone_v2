#!/usr/bin/python3
"""
Title: Deploy archive!
Description: Fabric script (based on the file 1-pack_web_static.py that
            distributes an archive to the web servers, using the function
            do_deploy
Author: a_idk
"""
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ['54.175.115.175', '54.237.55.177']  # my web servers


def do_deploy(archive_path):
    """
    Method that distributes an archive to my web servers
    """
    # check if path exist
    if exists(archive_path) is False:
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
