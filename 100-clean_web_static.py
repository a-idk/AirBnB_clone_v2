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

    # list of files in directory
    arch = sorted(os.listdir("versions"))
    # remove items from end of list
    for i in range(number):
        arch.pop()
    # delete files in directory
    with lcd("versions"):
        for f_name in arch:
            local(f"rm ./{f_name}")
    # get list of files in release directory
    with cd("/data/web_static/releases"):
        arch = run("ls -tr").split()
        # filter list
        filt_arch = []
        for f_name in arch:
            if "web_static_" in f_name:
                filt_arch.append(f_name)
        arch = filt_arch
        # remove items from end of list
        for j in range(number):
            arch.pop()
        # delete files from release directory
        for f_name in arch:
            run(f"rm -rf ./{f_name}")
