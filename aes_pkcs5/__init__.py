from importlib.metadata import metadata
from sys import version_info

_pkg_info = metadata("aes_pkcs5")

__version__ = _pkg_info["Version"]
__author__ = _pkg_info["Author"]

__all__ = ("__version__", "__author__")
