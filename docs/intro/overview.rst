=================
Overview
=================
AESPKCS5 supports two outputs formats: Base64 (``b64``) and hexadecimal (``hex``) and key size of: ``128``, ``192`` and
``256`` bits.

AESCommon
=========
This is a abstract class that others classes inherit and implement the abstract method ``_get_cipher``

.. warning::

    You can't instantiate abstract class ``AESCommon`` directly.

.. autoclass:: aes_pkcs5.algorithms.AESCommon
    :members:
    :private-members:


AESCBCPKCS5Padding
==================
This class implements the AES algorithm with CBC mode of operation and padding scheme PKCS5.

.. autoclass:: aes_pkcs5.algorithms.aes_cbc_pkcs5_padding.AESCBCPKCS5Padding
    :members:
    :private-members:
    :show-inheritance:

Example::

    from aes_pkcs5.algorithms.aes_cbc_pkcs5_padding import AESCBCPKCS5Padding


    # b64
    key = "@NcRfUjXn2r5u8x/"
    output_format = "b64"
    iv_parameter = "0011223344556677"
    message = "Hello World"

    cipher = AESCBCPKCS5Padding(key, output_format, iv_parameter)
    encrypted = cipher.encrypt(message)
    assert encrypted == "MhL/V78kC3rcYlnlPg1L4g=="
    assert cipher.decrypt(encrypted) == message

    # hex
    output_format = "hex"
    cipher = AESCBCPKCS5Padding(key, output_format, iv_parameter)
    encrypted = cipher.encrypt("Hello World")
    assert encrypted == "3212ff57bf240b7adc6259e53e0d4be2"
    assert cipher.decrypt(encrypted) == message

AESECBPKCS5Padding
==================

.. autoclass:: aes_pkcs5.algorithms.aes_ecb_pkcs5_padding.AESECBPKCS5Padding
    :members:
    :private-members:
    :show-inheritance:

Example::

    from aes_pkcs5.algorithms.aes_ecb_pkcs5_padding import AESECBPKCS5Padding

    # b64
    key = "@NcRfUjXn2r5u8x/"
    output_format = "b64"
    message = "Hello World"

    cipher = AESECBPKCS5Padding(key, output_format)
    encrypted = cipher.encrypt(message)
    assert encrypted == "CbU8DWZYXs00yq6F8ZNXGQ=="
    assert cipher.decrypt(encrypted) == message


    # hex
    output_format = "hex"
    cipher = AESECBPKCS5Padding(key, output_format)
    encrypted = cipher.encrypt(message)
    assert encrypted == "09b53c0d66585ecd34caae85f1935719"
    assert cipher.decrypt(encrypted) == message
