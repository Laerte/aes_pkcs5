from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC

from aes_pkcs5.algorithms import AESCommon, Cipher


class AESCBCPKCS5Padding(AESCommon):
    """
    Implements AES algorithm with CBC mode of operation and padding scheme PKCS5.
    """

    def __init__(self, key: str, output_format: str, iv_parameter: str):
        super(AESCBCPKCS5Padding, self).__init__(key=key, output_format=output_format)
        self._iv_parameter = iv_parameter.encode()

    def _get_cipher(self):
        """Return AES/CBC/PKCS5Padding Cipher"""
        return Cipher(
            AES(self._key), mode=CBC(self._iv_parameter), backend=default_backend()
        )
