#!/usr/local/bin/python3

import doctest
import glob
import json
import os
import pathlib
import subprocess
import sys


THIS_DIR = pathlib.Path(__file__).resolve().parent
ENGLISH_WORDS_FILEPATH = os.path.join(THIS_DIR, "english.txt")

DIGIT_TO_LETTER = {
    # T and D have one downstroke.
    1: "td",

    # N has two downstrokes.
    3: "m",

    # M has three downstrokes.
    2: "n",

    # In English, four ends with an R.
    4: "r",

    # In Latin, L means 50.
    5: "l",

    # Lowercase j looks like a 6.
    6: "j",

    # K looks like two 7s, and g sounds similar to k.
    7: "kg",

    # Handwritten lowercase f looks like an 8, and v sounds similar to f.
    8: "fv",

    # P in a mirror looks similar to 9.
    9: "p",

    # Zero starts with a z, and s sounds similar to z.
    0: "zs",
}


class Converter:

    def __init__(self):
        super().__init__()

        self.init_letters_to_digits()
        self.init_words()
        self.init_number_to_words()

    def init_letters_to_digits(self):
        """
        >>> converter = Converter()
        >>> converter.LETTER_TO_DIGIT["t"]
        1
        >>> converter.LETTER_TO_DIGIT["d"]
        1
        >>> converter.LETTER_TO_DIGIT["n"]
        2
        """
        self.LETTER_TO_DIGIT = {}

        # TODO: complete this function to pass the doc-tests.

    def init_words(self):
        """
        >>> converter = Converter()
        >>> "english" in converter.WORDS
        True
        """

        # TODO: complete this function to load the words in
        # `ENGLISH_WORDS_FILEPATH`.
        self.WORDS = []

    def word_to_number(self, word):
        """
        >>> converter = Converter()
        >>> converter.word_to_number("dynamo")
        '123'
        >>> converter.word_to_number("university")
        '28401'
        """

        # TODO: complete this function to pass the doc-tests.
        pass

    def init_number_to_words(self):
        """
        >>> converter = Converter()
        >>> converter.NUMBER_TO_WORDS.get('5985', '')
        ['helpful', 'lapful', 'loopful']
        """
        self.NUMBER_TO_WORDS = {}

        # TODO: complete this function to pass the doc-tests.
        pass

    def number_to_words(self, number_str):
        """
        >>> converter = Converter()
        >>> converter.number_to_words('5985')
        ['helpful', 'lapful', 'loopful']
        """

        # TODO: complete this function to pass the doc-tests.


def main():
    # Students: this `main()` function serves to use the converter
    # from the command-line. You can ignore it.

    converter = Converter()

    while True:
        number_str = input("Please enter a number to convert to a word: ")
        try:
            words = converter.number_to_words(number_str)
        except ValueError:
            print("You did not enter a number")
            continue

        if not words:
            print("> There are no English words for this number")
        else:
            print(f"> The English words for number {number_str} are:")
            print("    " + "\n    ".join(words), sep="")


if '__main__' == __name__:
    doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)
    assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'
    print("All doc-tests pass, proceeding with script...")
    main()
