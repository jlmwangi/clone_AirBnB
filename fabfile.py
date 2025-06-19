#!/usr/bin/python3
'''create and distribute an archive to my web servers'''

from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy

def deploy():
    try:
        path = do_pack()
        if not path:
            return False
        return do_deploy(path)

    except Exception as e:
        return False
    
