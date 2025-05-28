#!/usr/bin/python3
'''a afbric script that generates tgz archive from contenets of web_static'''


from fabric import task


@task
def do_pack(c):
    '''files in web_static must be added to final archive
       all archives stored in folder versions which is created it it doesnt exist
       fn returns archive path if archive has been correctly generated
    '''

    import os
    from datetime import datetime

    versions_dir = "versions"
    os.makedirs(versions_dir, exist_ok=True)

    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{dt}.tgz"
    archive_path = os.path.join(versions_dir, archive_name)

    print(f"Packing web_static to {archive_path}")

    result = c.run(f"tar -czvf {archive_path} web_static")
    if result.ok:
        print(f"web_static packed: {archive_path}")
        return archive_path
    else:
        return None
