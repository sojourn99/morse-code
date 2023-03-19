from morse import convert_to_morse_code, convert_from_morse_code, validate_morse_code, validate_text_input
import pytest


def test_validate_text_input_correct():
    assert validate_text_input("SOS")
    assert validate_text_input("This is test number 17")


def test_validate_text_input_incorrect():
    assert not validate_text_input("SOS!")


def test_validate_morse_input_correct():
    assert validate_morse_code(". . .")


def test_validate_morse_input_incorrect():
    assert not validate_morse_code(". - @")


def test_morse_encode_correct_input():
    assert convert_to_morse_code("sos") == "● ● ●   ■■■ ■■■ ■■■   ● ● ●"
    assert convert_to_morse_code("sos sos") == "● ● ●   ■■■ ■■■ ■■■   ● ● ●       ● ● ●   ■■■ ■■■ ■■■   ● ● ●"
    assert convert_to_morse_code("this is test number 17") == "■■■   ● ● ● ●   ● ●   ● ● ●       ● ●   ● ● ●       ■■■   ●   ● ● ●   ■■■       ■■■ ●   ● ● ■■■   ■■■ ■■■   ■■■ ● ● ●   ●   ● ■■■ ●       ● ■■■ ■■■ ■■■ ■■■   ■■■ ■■■ ● ● ●"


def test_morse_encode_incorrect_input():
    with pytest.raises(Exception) as exc_info:
        convert_to_morse_code("@")
    assert str(exc_info.value) == "Cannot encode character: @"


def test_morse_decode_correct_input():
    assert convert_from_morse_code(". . .   - - -   . . .") == "sos"
    assert convert_from_morse_code(". . .   - - -   . . .       . . .   - - -   . . .") == "sos sos"
    assert convert_from_morse_code("-   . . . .   . .   . . .       . .   . . .       -   .   . . .   -       - .   . . -   - -   - . . .   .   . - .       . - - - -   - - . . .") == "this is test number 17"


def test_morse_decode_incorrect_input():
    # no space separation
    with pytest.raises(Exception) as exc_info:
        convert_from_morse_code("...")
    assert str(exc_info.value) == "Cannot decode morse code symbol: ..."

    # non existent morse symbol
    with pytest.raises(Exception) as exc_info:
        convert_from_morse_code("- - - -")
    assert str(exc_info.value) == "Cannot decode morse code symbol: - - - -"
