from vigenere_cipher import VigenereCipher
from unittest.mock import patch, Mock
import pytest

@pytest.fixture()
def train_cipher():
    return VigenereCipher("TRAIN")

def test_init():
    cipher = VigenereCipher("TRAIN")
    assert hasattr(cipher, "keyword")
    assert cipher.keyword == "TRAIN"

def test_encode(train_cipher):
    encoded = train_cipher.encode("ENCODEDINPYTHON")
    assert encoded == "XECWQXUIVCRKHWA"

def test_code_mocked(train_cipher):
    # This test has been fixed from the version shown in class on 10/11/21.
    # If we ran it before it would have failed because the mocks were not
    # realistic enough. We fix this by setting some return values. Try messing
    # around with this example to see how you can use Mock objects. 
    with patch.object(train_cipher, "extend_keyword") as extend:
        extend.return_value = "TRA"
        combine = Mock()
        combine.return_value = "/ join_test /"
        assert train_cipher._code("ENC", combine) == "/ join_test // join_test // join_test /"
        extend.assert_called_once_with(len("ENC"))
        combine.assert_any_call("E", "T")
        combine.assert_any_call("N", "R")
        combine.assert_called_with("C", "A")

def test_encode_character(train_cipher):
    encoded = train_cipher.encode("E")
    assert encoded == "X"


def test_encode_spaces():
    cipher = VigenereCipher("TRAIN")
    encoded = cipher.encode("ENCODED IN PYTHON") 
    assert encoded == "XECWQXUIVCRKHWA"


def test_encode_lowercase():
    cipher = VigenereCipher("TRain")
    encoded = cipher.encode("encodedinPython")
    assert encoded == "XECWQXUIVCRKHWA"


def test_combine_character():
    assert VigenereCipher.combine_character("E", "T") == "X"
    assert VigenereCipher.combine_character("N", "R") == "E"


def test_extend_keyword():
    cipher = VigenereCipher("TRAIN")
    extended = cipher.extend_keyword(16)
    assert extended == "TRAINTRAINTRAINT"
    extended = cipher.extend_keyword(15)
    assert extended == "TRAINTRAINTRAIN"


def test_separate_character():
    assert VigenereCipher.separate_character("X", "T") == "E"
    assert VigenereCipher.separate_character("E", "R") == "N"


def test_decode():
    cipher = VigenereCipher("TRAIN")
    decoded = cipher.decode("XECWQXUIVCRKHWA")
    assert decoded == "ENCODEDINPYTHON"