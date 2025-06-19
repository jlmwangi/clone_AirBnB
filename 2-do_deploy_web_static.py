#!/usr/bin/python3
'''a fabric script that distributes archive to web servers'''

from fabric import task, Connection
import os

hosts = ['xx-web-01', 'xx-web-02']

@task
def do_deploy(c, archive_path):
    '''check if file aat archive_path exists'''
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        folder_name = archive_filename.replace('.tgz', '')
        release_path = f'/data/web_static/releases/{folder_name}/'

        for host in hosts:
            c = Connection(host)
            '''upload archive to tmp dir of webserver'''
            c.put(archive_path, '/tmp/')

            #create release path
            c.run(f'mkdir -p {release_path}')
            #extract archive to release path
            c.run(f'tar -xzf /tmp/{archive_filename} -C {release_path}')
            #move contents out of web_static folder
            c.run(f'mv {release_path}web_static/* {release_path}')
            c.run(f'rm -rf {release_path}web_static')

            #clean up archive
            c.run(f'rm /tmp/{archive_filename}')

            #remove old sym link
            c.run('rm -rf /data/web_static/current')
            c.run(f'ln -s {release_path} /data/web_static/current')

        return True

    except Exception as e:
        print(f'Deployment failed: {e}')
        return False
