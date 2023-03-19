import argparse
import re

# International Morse code
# The length of a dot is one unit, dit: . ●
# A dash is three units, dah: - ■■■ (three dits)
# The space between parts of the same letter is one unit (signal absence): space character
# The space between letters is three units.
# The space between words is seven units.

morse_encode = {
    "a": "● ■■■",
    "b": "■■■ ● ● ●",
    "c": "■■■ ● ■■■ ●",
    "d": "■■■ ● ●",
    "e": "●",
    "f": "● ● ■■■ ●",
    "g": "■■■ ■■■ ●",
    "h": "● ● ● ●",
    "i": "● ●",
    "j": "● ■■■ ■■■ ■■■",
    "k": "■■■ ● ■■■",
    "l": "● ■■■ ● ●",
    "m": "■■■ ■■■",
    "n": "■■■ ●",
    "o": "■■■ ■■■ ■■■",
    "p": "● ■■■ ■■■ ●",
    "q": "■■■ ■■■ ● ■■■",
    "r": "● ■■■ ●",
    "s": "● ● ●",
    "t": "■■■",
    "u": "● ● ■■■",
    "v": "● ● ● ■■■",
    "w": "● ■■■ ■■■",
    "x": "■■■ ● ● ■■■",
    "y": "■■■ ● ■■■ ■■■",
    "z": "■■■ ■■■ ● ●",
    "1": "● ■■■ ■■■ ■■■ ■■■",
    "2": "● ● ■■■ ■■■ ■■■",
    "3": "● ● ● ■■■ ■■■",
    "4": "● ● ● ● ■■■",
    "5": "● ● ● ● ●",
    "6": "■■■ ● ● ● ●",
    "7": "■■■ ■■■ ● ● ●",
    "8": "■■■ ■■■ ■■■ ● ●",
    "9": "■■■ ■■■ ■■■ ■■■ ●",
    "0": "■■■ ■■■ ■■■ ■■■ ■■■",
    " ": "       "
}

morse_decode = {
    ". -": "a",
    "- . . .": "b",
    "- . - .": "c",
    "- . .": "d",
    ".": "e",
    ". . - .": "f",
    "- - .": "g",
    ". . . .": "h",
    ". .": "i",
    ". - - -": "j",
    "- . -": "k",
    ". - . .": "l",
    "- -": "m",
    "- .": "n",
    "- - -": "o",
    ". - - .": "p",
    "- - . -": "q",
    ". - .": "r",
    ". . .": "s",
    "-": "t",
    ". . -": "u",
    ". . . -": "v",
    ". - -": "w",
    "- . . -": "x",
    "- . - -": "y",
    "- - . .": "z",
    ". - - - -": "1",
    ". . - - -": "2",
    ". . . - -": "3",
    ". . . . -": "4",
    ". . . . .": "5",
    "- . . . .": "6",
    "- - . . .": "7",
    "- - - . .": "8",
    "- - - - .": "9",
    "- - - - -": "0",
    "   ": "",
    "       ": " "
}


def main():
    parser = argparse.ArgumentParser(prog="morse.py",
                                     description="Encodes text to Morse and decodes Morse code to text")
    parser.add_argument("-d", "--direction", choices=["encode", "decode"], help="select encode or decode", type=str)
    args = parser.parse_args()

    if args.direction == "encode":
        text_input = input("Text: ").lower()
        if validate_text_input(text_input):
            print(convert_to_morse_code(text_input))
        else:
            print("Invalid input")
    else:
        morse_code_input = input("Morse code: ")
        if validate_morse_code(morse_code_input):
            print(convert_from_morse_code(morse_code_input))
        else:
            print("Invalid input")


def validate_text_input(text: str):
    """
    Validates text input. Permitted are lower- and uppercase letters and digits.

    :param text: text to be validated
    :type text: str
    :return: True or False
    :rtype: boolean
    """
    return re.search(r"^[a-zA-Z0-9 ]+$", text)


def validate_morse_code(morse_code: str):
    """
    Validates morse code input. Permitted are dots (.), dashes (-) and space characters.

    :param morse_code: code to be validated
    :type morse_code: str
    :return: True or False
    :rtype: boolean
    """
    return re.search(r"^[\.\- ]+$", morse_code)


def convert_from_morse_code(code: str):
    """
    Decodes morse code to text.

    :param code: the morse code to be decoded
    :type code: str
    :return: decoded morse code
    :rtype: str
    """
    text = ""
    words = code.split("       ")

    if not words:
        words = [code]

    for word in words:
        chars = word.split("   ")

        for char in chars:
            try:
                text += morse_decode[char]
            except KeyError as e:
                raise Exception(f"Cannot decode morse code symbol: {char}") from e
        # separate words by one space
        text += " "

    return text.strip()


def convert_to_morse_code(text: str):
    """
    Encodes text to morse code.

    :param text: the text to be encoded
    :type text: str
    :return: encoded text
    :rtype: str
    """
    code = ""
    words = text.split(" ")
    if not words:
        words = [text]
    for word in words:
        for char in word:
            try:
                # separate each symbol by three spaces
                code += morse_encode[char] + "   "
            except KeyError as e:
                raise Exception(f"Cannot encode character: {char}") from e
        # add 4 spaces to separate words by 7 spaces
        code += "    "
    return code.strip()


if __name__ == "__main__":
    main()
