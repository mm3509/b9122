import os
import pathlib

from nltk.corpus import words

# Run this once only, to download NLTK's English words.
# import nltk
# nltk.download("words")

import exercise_7_pin


english_words = words.words()
english_lower = [w.lower() for w in english_words]
english_set = set(english_lower)
english_sorted = sorted(english_set)


with open(exercise_7_pin.DATA_FILEPATH, 'w+', encoding='utf-8') as f:
    f.write("\n".join(english_sorted))
