#!/usr/bin/python3


"""pack and compress web_static dir"""


from datetime import datetime
from pathlib import Path


from fabric.api import local


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

    yymmdd = f"{now.year}{now.month: 02.0f}{now.day: 02.0f}"
    hhmmss = f"{now.hour: 02.0f}{now.minute: 02.0f}{now.second: 02.0f}"

    file_name = f"{src}_{yymmdd}{hhmmss}.tgz"
    full_path = f"{dest}/{file_name}"

    return full_path


def _create_dir(dest):
    """create path object mapped to path on system"""

    path = Path(dest)

    if not path.is_dir():
        path.mkdir()
