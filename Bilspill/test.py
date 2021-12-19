

from sys import platform


def os_version():
    if platform == "win32":
        return True
    elif platform == "darwin":
        return False

