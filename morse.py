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
    "       ": " "
}


def main():
    # TODO validate text input with regex
    # TODO validate morse code input with regex
    # TODO use command line argument to select morse encode or decode
    parser = argparse.ArgumentParser(description="Morse encode/decode")
    parser.add_argument("-c", default="encode", help="select encode or decode", type=str)
    args = parser.parse_args()
    print(args.c)
    if args.c == "encode":
        print(convert_to_morse_code(input("Text: ").lower()))
    else:
        pass


def convert_to_morse_code(text: str):
    code = ""
    for char in text:
        try:
            code += morse_encode[char] + "   "
        except KeyError:
            raise KeyError(f"Cannot encode character {char}")
    return code.strip()


if __name__ == "__main__":
    main()
