# isort: skip_file
from typing import Dict, List

from pytest import mark

from aes_pkcs5.algorithms.aes_cbc_pkcs5_padding import AESCBCPKCS5Padding
from tests.algorithms import (
    _128_BITS_KEY,
    _192_BITS_KEY,
    _256_BITS_KEY,
    INPUT_VALUE,
    IV,
    OUTPUT_FORMATS,
)


@mark.parametrize(
    "key, expected_outputs",
    [
        (
            _128_BITS_KEY,
            {
                "b64": "1UbdgSeSNoAtWZ2AEd1I7C5yZNbqJ8F7VGBBN7k1FSXUW2lV30NctsgZzRff75ru",
                "hex": "d546dd81279236802d599d8011dd48ec2e7264d6ea27c17b54604137b9351525d45b6955df435cb6c819cd17dfef9aee",
            },
        ),
        (
            _192_BITS_KEY,
            {
                "b64": "dg3CcXuvLL4p2jJHlKEryoUZT7olXqKjuGvSrxha15irqZM/9WD/7ZFPZQtt0+16",
                "hex": "760dc2717baf2cbe29da324794a12bca85194fba255ea2a3b86bd2af185ad798aba9933ff560ffed914f650b6dd3ed7a",
            },
        ),
        (
            _256_BITS_KEY,
            {
                "b64": "BtXP7+nujvnE5tn+uHiwkkpgwNymp2rkO0aJCvrF+56Zx+M2yAQb1w6yYN4u2xqP",
                "hex": "06d5cfefe9ee8ef9c4e6d9feb878b0924a60c0dca6a76ae43b46890afac5fb9e99c7e336c8041bd70eb260de2edb1a8f",
            },
        ),
    ],
)
def test_encrypt_and_decrypt_and_output_formats(
    key: str, expected_outputs: Dict[str, List[str]]
):
    for output_format in OUTPUT_FORMATS:
        cipher = AESCBCPKCS5Padding(key, output_format, IV)
        encrypted_output = cipher.encrypt(INPUT_VALUE)
        assert encrypted_output == expected_outputs.get(output_format)
        assert cipher.decrypt(encrypted_output) == INPUT_VALUE
