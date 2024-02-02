#!/usr/bin/python3
"""
Title: Compress before sending
Description: Fabric script that generate a .tgz archive from the contents
            of the web_static folder of AirBnB clone repo
author: a_idk
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """
    method that compresses the webstatic repo
    """
    dt = datetime.now()
    arch = 'web_static_' + dt.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local("mkdir -p versions")
    comp = local(f'tar -cvzf versions/{arch} web_static')
    # create = local('tar -cvzf versions/{} web_static'.format(archive))

    # returning archinve path if created
    if comp is not None:
        return arch
    else:
        return None
