# isort: skip_file
from typing import Dict, List

from pytest import mark

from aes_pkcs5.algorithms.aes_ecb_pkcs5_padding import AESECBPKCS5Padding
from tests.algorithms import (
    _128_BITS_KEY,
    _192_BITS_KEY,
    _256_BITS_KEY,
    INPUT_VALUE,
    OUTPUT_FORMATS,
)


@mark.parametrize(
    "key, expected_outputs",
    [
        (
            _128_BITS_KEY,
            {
                "b64": "D26uvwXiwnU8tORKQ78iPOftTchRd7kO12PUYetpFELijn9XedBXpc20u/j5+bl6",
                "hex": "0f6eaebf05e2c2753cb4e44a43bf223ce7ed4dc85177b90ed763d461eb691442e28e7f5779d057a5cdb4bbf8f9f9b97a",
            },
        ),
        (
            _192_BITS_KEY,
            {
                "b64": "K7S7QPvKgwnf39C9tAKwdzMiBQzp/ItZrrNL9xXGn2Nl+S+OzFB9bq7NaNc/a5WK",
                "hex": "2bb4bb40fbca8309dfdfd0bdb402b0773322050ce9fc8b59aeb34bf715c69f6365f92f8ecc507d6eaecd68d73f6b958a",
            },
        ),
        (
            _256_BITS_KEY,
            {
                "b64": "mVsyT1OKSbGH0aFqUYDHcT415TRRfKewNN5sMTMffh0ZkfcDDm4rcJOYtESs8MKH",
                "hex": "995b324f538a49b187d1a16a5180c7713e35e534517ca7b034de6c31331f7e1d1991f7030e6e2b709398b444acf0c287",
            },
        ),
    ],
)
def test_encrypt_and_decrypt_and_output_formats(
    key: str, expected_outputs: Dict[str, List[str]]
):
    for output_format in OUTPUT_FORMATS:
        cipher = AESECBPKCS5Padding(key, output_format)
        encrypted_output = cipher.encrypt(INPUT_VALUE)
        assert encrypted_output == expected_outputs.get(output_format)
        assert cipher.decrypt(encrypted_output) == INPUT_VALUE
