import doctest
import os
import pathlib


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
        self.__init_letters_to_digits()
        self.__init_words()
        self.__init_number_to_words()

    def __init_letters_to_digits(self):
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
        for digit, letters in DIGIT_TO_LETTER.items():
            for letter in letters:
                self.LETTER_TO_DIGIT[letter] = digit

    def __init_words(self):
        """
        >>> converter = Converter()
        >>> "english" in converter.WORDS
        True
        """
        with open(ENGLISH_WORDS_FILEPATH) as f:
            contents = f.read()
        self.WORDS = contents.split('\n')

    def word_to_number(self, word):
        """
        >>> converter = Converter()
        >>> converter.word_to_number("dynamo")
        '123'
        >>> converter.word_to_number("university")
        '28401'
        >>> converter.word_to_number(123)
        Traceback (most recent call last):
        ...
        AssertionError...
        """

        # For simplicity in doc-tests, this is not a private method.

        assert isinstance(word, str)

        assert self.LETTER_TO_DIGIT, "letters to digit uninitialized"

        number_str = ""
        for letter in word:
            number_str += str(self.LETTER_TO_DIGIT.get(letter, ""))

        if "" == number_str:
            return None

        # Don't convert to integer, otherwise you lose the leading zero.
        return number_str

    def __init_number_to_words(self):
        """
        >>> converter = Converter(); converter.NUMBER_TO_WORDS.get('5985', '')
        ['helpful', 'lapful', 'loopful']
        """
        self.NUMBER_TO_WORDS = {}
        for word in self.WORDS:

            number_str = self.word_to_number(word)
            if None is number_str:
                continue

            if number_str not in self.NUMBER_TO_WORDS:
                self.NUMBER_TO_WORDS[number_str] = []

            self.NUMBER_TO_WORDS[number_str].append(word)

    def number_to_words(self, number_str):
        """
        >>> converter = Converter()
        >>> converter.number_to_words('5985')
        ['helpful', 'lapful', 'loopful']
        >>> converter.number_to_words('abc')
        Traceback (most recent call last):
        ...
        AssertionError...
        """
        try:
            int(number_str)
        except ValueError:
            assert False, "argument must be a string with a number"

        number_str_clean = number_str.strip()
        words = self.NUMBER_TO_WORDS.get(number_str_clean, [])
        return sorted(words)


def main():
    # Students: this `main()` function serves to use the converter from the
    # command-line, in case you want to use it for your own benefit. For the
    # purpose of the assignment, you can ignore this.

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


# Students: this is how you can run code when calling from the shell or
# command-line, but not when importing the file.
if '__main__' == __name__:

    # Students: these two lines prevent execution of the script unless the
    # doc-tests pass.
    doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)
    assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'
    main()
