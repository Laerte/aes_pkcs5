from importlib.metadata import metadata

__version__, __author__ = list(
    map(lambda x: metadata("aes_pkcs5")[x], ["Version", "Author"])
)

__all__ = ("__version__", "__author__")
