from abc import ABCMeta, abstractmethod
from base64 import b64decode, b64encode
from binascii import unhexlify

from cryptography.hazmat.primitives.ciphers import Cipher

OUTPUT_FORMATS = ("b64", "hex")


class AESCommon(metaclass=ABCMeta):
    """Common AES interface"""

    def __init__(self, key: str, output_format: str) -> None:
        self._key = key.encode()

        if output_format not in OUTPUT_FORMATS:
            raise NotImplementedError(
                f"Support for output format: {output_format} is not implemented"
            )

        self._output_format = output_format

    def encrypt(self, message: str) -> str:
        """
        Return encrypted message

        :param message: message to be encrypted
        :type message: str
        """
        cipher_instance = self._get_cipher()
        message = message.encode()

        offset = 16 - len(message) % 16
        message = message + (offset * chr(offset)).encode()

        encryptor = cipher_instance.encryptor()

        result = encryptor.update(message)

        return (
            b64encode(result).decode() if self._output_format == "b64" else result.hex()
        )

    def decrypt(self, message: str) -> str:
        """
        Return decrypted message

        :param message: encrypted message
        :type message: str
        """
        cipher_instance = self._get_cipher()

        decryptor = cipher_instance.decryptor()

        result = decryptor.update(
            b64decode(message) if self._output_format == "b64" else unhexlify(message)
        )

        pad_num = result[-1]
        result = result[:-pad_num]

        return result.decode()

    @abstractmethod
    def _get_cipher(self) -> Cipher:
        """
        Return the Cipher that will be used
        """
