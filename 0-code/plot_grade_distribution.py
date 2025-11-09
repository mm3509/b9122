import os
import pathlib
import random


import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


THIS_DIR = pathlib.Path(__file__).resolve().parent
PROGRAM_COL = "program"
GRADE_COL = "grade"


def summarize_grades(filename):
    assert isinstance(filename, str)
    assert filename.endswith(".csv")
    filepath = os.path.join(THIS_DIR, filename)
    assert os.path.exists(filepath)

    df = pd.read_csv(filepath)
    assert PROGRAM_COL in df.columns
    assert GRADE_COL in df.columns
    
    programs = df[PROGRAM_COL].unique()

    minimum = 0
    maximum = 140
    num_bins = 20
    bins = np.linspace(minimum, maximum, num_bins)

    x = [random.gauss(3,1) for _ in range(400)]
    y = [random.gauss(4,2) for _ in range(400)]

    for program in programs:
        program_df = df[df[PROGRAM_COL] == program]
        program_grades = program_df[GRADE_COL]

        print("*" * 80)
        print("Summary statistics for program:", program)
        print(program_grades.describe())

        plt.hist(program_grades, bins, alpha=0.5, label=program)
        plt.title(program)
        plt.savefig(program + ".png")
        plt.show()


if '__main__' == __name__:
    summarize_grades("midterm-anonymized.csv")
