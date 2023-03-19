# Text to Morse Code Convertor
#### [Video Demo](https://youtu.be/FSZZMX1bZM4)
#### Description:
This project is a text-based (command-line) Python program to convert Strings into International Morse Code, and Morse Code into text. 
It takes any String text input and encodes this to Morse code, as well takes any Morse code input to decode to text.
[See this Wikipedia article for more information about Morse code](https://en.wikipedia.org/wiki/Morse_code)

Short explanation of International Morse code:

![International Morse code](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/International_Morse_Code.svg/390px-International_Morse_Code.svg.png)

+ The length of a dot is one unit, dit: `.` or `●`. 
+ A dash is three units, dah: `-` or `■■■` (three dits). 
+ The space between parts of the same letter is one unit (signal absence): space character. 
+ The space between letters is three units.
+ The space between words is seven units.

To run the program:
```
python .\morse.py [-h] [-d {encode,decode}]
```

Command line arguments:
```
options:
  -h, --help            show this help message and exit
  -d {encode,decode}, --direction {encode,decode}
                        select encode or decode
```

When entering Morse code use the dot character `.` for a 'dit', a dash character `-` for a 'dah', and a space character for one unit of signal absence.

All functions of program morse.py are documented using Docstrings.
Function `main()` processes the input and makes calls to the validation and conversion functions.
The program uses the `argparse` module for the command-line interface.
Regular expressions (module `re`) are used to validate the input (functions `validate_text_input()` and `validate_morse_code()`). 
When input is not valid the output of the program will be: "Invalid input". 

The functions `convert_to_morse_code()` and `convert_from_morse_code()` are responsible for the conversion. 
To be able to convert each text character a dictionary is used with the characters as keys and the corresponding Morse code symbols as values.
To be able to convert each Morse code symbol a dictionary is used with the Morse code symbols as keys and the corresponding text characters as values. 
When a character or Morse code symbol is not available in the respective dictionaries an exception is raised with an appropriate message to the user.

File test_morse.py contains several unit tests for testing correct and incorrect input, the conversion functions and whether the expected exception is raised when encoding or decoding fails. 
Module pytest is needed to run these tests:
```
pytest .\test_morse.py
```

