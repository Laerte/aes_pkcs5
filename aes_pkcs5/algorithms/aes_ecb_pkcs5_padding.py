from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import ECB

from aes_pkcs5.algorithms import AESCommon, Cipher


class AESECBPKCS5Padding(AESCommon):
    """
    Implements AES algorithm with ECB mode of operation and padding scheme PKCS5.
    """

    def __init__(self, key: str, output_format: str):
        super(AESECBPKCS5Padding, self).__init__(key=key, output_format=output_format)

    def _get_cipher(self):
        """Return AES/CBC/PKCS5Padding Cipher"""
        return Cipher(AES(self._key), mode=ECB(), backend=default_backend())
