from pytest import raises

from aes_pkcs5.algorithms import AESCommon


class DummyCipher(AESCommon):
    def _get_cipher(self):
        return "dummy_cipher"


def test_not_implemented_output_format():
    with raises(NotImplementedError) as exc_info:
        DummyCipher("key", "json")

    assert f"{exc_info.value}" == "Support for output format: json is not implemented"


def test_dummy_get_cipher():
    assert DummyCipher("key", "b64")._get_cipher() == "dummy_cipher"
