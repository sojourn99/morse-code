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
    # TODO proces file with text/morse code, output to file
    # TODO add README.md
    # TODO add requirements.txt

    parser = argparse.ArgumentParser(description="Morse encode/decode")
    parser.add_argument("-c", default="encode", help="select encode or decode", type=str)
    args = parser.parse_args()
    print(args.c)
    if args.c == "encode":
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


def validate_text_input(text):
    return re.search(r"^[a-zA-Z0-9]+$", text)


def validate_morse_code(morse_code):
    return re.search(r"^[\.\- ]+$", morse_code)


def convert_from_morse_code(code: str):
    text = ""
    words = code.split("       ")

    if not words:
        words = [code]

    for word in words:
        chars = word.split("   ")

        for char in chars:
            try:
                text += morse_decode[char]
            except KeyError:
                raise KeyError(f"Cannot decode morse code symbol: {char}")
        # separate words by one space
        text += " "

    return text.strip()


def convert_to_morse_code(text: str):
    code = ""
    words = text.split(" ")
    if not words:
        words = [text]
    for word in words:
        for char in word:
            try:
                # separate each symbol by three spaces
                code += morse_encode[char] + "   "
            except KeyError:
                raise KeyError(f"Cannot encode character: {char}")
        # add 4 spaces to separate words by 7 spaces
        code += "    "
    return code.strip()


if __name__ == "__main__":
    main()
