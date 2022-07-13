from sys import version_info

if version_info >= (3, 8):
    from importlib.metadata import metadata
else:
    from importlib_metadata import metadata

_pkg_info = metadata("aes_pkcs5")

__version__ = _pkg_info["Version"]
__author__ = _pkg_info["Author"]

__all__ = ("__version__", "__author__")
