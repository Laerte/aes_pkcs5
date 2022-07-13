from sys import version_info

if version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version

__version__ = version("aes_pkcs5")
