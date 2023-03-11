from morse import convert_to_morse_code, convert_from_morse_code
import pytest


def test_morse_encode_correct_input():
    assert convert_to_morse_code("sos") == "● ● ●   ■■■ ■■■ ■■■   ● ● ●"


def test_morse_encode_incorrect_input():
    with pytest.raises(KeyError):
        convert_to_morse_code("@")


def test_morse_decode_correct_input():
    assert convert_from_morse_code(". . .   - - -   . . .") == "sos"


def test_morse_decode_incorrect_input():
    with pytest.raises(KeyError):
        convert_from_morse_code("...")
