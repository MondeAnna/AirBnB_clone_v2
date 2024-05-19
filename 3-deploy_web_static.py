#!/usr/bin/python3


"""archive and deploy web_static dir"""


from datetime import datetime
from pathlib import Path


from fabric.api import env, local, put, run


env.hosts = ["18.207.235.144", "54.209.218.24"]


def deplay():
    """archive and deploy web_static"""

    archive_path = do_pack()
    return do_deploy(archive_path)


def do_deploy(archive_path):
    """deploy web_static archive"""

    curr_dir = "/data/web_static/current"

    if not Path(archive_path).is_file():
        return False

    archive_name = archive_path.split("/")[-1]
    archive_dir = archive_name.replace(".tgz", "")
    release_dir = f"/data/web_static/releases/{archive_dir}"

    try:
        put(archive_path, f"/tmp/{archive_name}")

        run(f"mkdir -p {release_dir}")
        run(f"tar -xzf /tmp/{archive_name} -C {release_dir}")
        run(f"rm /tmp/{archive_name}")

        run(f"mv {release_dir}/web_static/* {release_dir}")
        run(f"rm -rf {release_dir}/web_static")
        run(f"rm -rf {curr_dir}")
        run(f"ln -s {release_dir} {curr_dir}")

        print("New version deployed!")
        return True
    except:
        return False


def do_pack():
    """archives files in `web_static`"""

    src = "web_static"
    dest = "versions"

    _create_dir(dest)
    full_path = _create_full_path(src, dest)

    print(f"Packing web_static to {full_path}")
    execution = local(f"tar -czvf {full_path} {src}")

    if execution.succeeded:
        file_size = Path(full_path).stat().st_size
        print(f"{src} packed: {full_path} -> {file_size}")

        return full_path

    return None


def _create_full_path(src, dest):
    """create string representation of system path to archive"""

    now = datetime.now()

    yymmdd = f"{now.year}{now.month:02.0f}{now.day:02.0f}"
    hhmmss = f"{now.hour:02.0f}{now.minute:02.0f}{now.second:02.0f}"

    file_name = f"{src}_{yymmdd}{hhmmss}.tgz"
    full_path = f"{dest}/{file_name}"

    return full_path


def _create_dir(dest):
    """create path object mapped to path on system"""

    path = Path(dest)

    if not path.is_dir():
        path.mkdir()
