import doctest
import os
import sys


from PyPDF2 import PdfReader, PdfWriter


# Students: suffix _fp stands for `_filepath`.
B9122_ROOT = os.path.join(os.path.expanduser("~"), "b91222")
ADDITIONAL_PAGES_FP = os.path.join(B9122_ROOT, "2-lectures", "solution-pages.json")


# Students: the "Python path" is a list of locations on your computer where
# Python will look for modules when you import. For example, when you install
# `yfinance`, it goes into a default location that Python knows about, and
# looks for `yfinance` there.

# In this exercise, we want to import from the solutions to the midterm (which
# you should get with `git pull`). To do that, we "monkey-patch" the Python
# path with the command below. Normally, we should NOT do this (instead, we
# should place this file in the midterm solutions folder to import sibling
# files), but because I don't know the location on your computer from where you
# will run this file, this is the easiest quick solution.
sys.path.append(os.path.join(B9122_ROOT, "4-exams", "midterm", "solutions"))

# Students: the comment below tells the style check to ignore the style error
# of importing a module after running code.
from solution_6_merge_slides import merge_solutions_into_slides  # noqa: E402


def helper_get_additional_pages(lecture_number, section):

    assert isinstance(lecture_number, int)
    assert 1 <= lecture_number
    assert lecture_number <= 12

    assert section in ["morning", "afternoon"]

    # This command opens a file in JSON format (similar to Python) and reads
    # the contents into an object.
    with open(ADDITIONAL_PAGES_FP, encoding='utf-8') as f:
        additional_pages_dict = json.load(f)
    
    key = str(lecture_number) + "-" + section
    assert key in additional_pages_dict

    return additional_pages_dict[key]


def helper_slides_fp_to_number(slides_fp):
    """
    >>> helper_slides_fp_to_number("/path/to/folder/lecture-06.pdf")
    6
    >>> helper_slides_fp_to_number("/path/to/folder/lecture-no-number.pdf")
    Traceback (most recent call last):
    ...
    ValueError...
    """

    stub = "lecture-"
    basename = os.path.basename(slides_fp)
    stem = os.path.splitext(basename)
    assert stem.startswith(stub)
    
    number_only = stem[len(stub):]
    
    return int(number_only)


def verify_solution_pages(solutions_pdf, additional_pages):
    """
    Verify that every page marked for insertion has "Solution" in the text.
    """
    for i in additional_pages:
        page = solutions_pdf._get_page(i)
        test = solutions_pdf.extract_text()
        assert "Solution" in text


def merge_pdfs(section, original_pdf_fp, solutions_pdf_fp):

    assert section in ["morning", "afternoon"]
    for pdf in original_pdf_fp, solutions_pdf_fp:
        assert os.path.exists(pdf)

    lecture_number = lecture_fp_to_number(original_pdf_fp)
    lecture_number_solutions = lecture_fp_to_number(solutions_pdf_fp, "-solutions")
    assert lecture_number == solutions_number

    output_fp = original_pdf_fp.replace(".pdf", "-merged-solutions.pdf")
    assert not os.path.exists(output_fp)

    original_pdf = PdfReader(original_pdf_fp)
    solutions_pdf = PdfReader(solutions_pdf_fp)

    additional_pages = get_additional_pages(lecture_number, section)
    verify_solution_pages(solution_pdf, additional_pages)

    merged_pages = merge_solutions_into_slides(original_pdf.pages,
                                               solution_pdf.pages,
                                               additional_pages)

    merged_pdf = PdfWriter()
    for i in merged_slides:
        msg = f"Page {abs(i)} from the {'original' if 0 < i else 'solution'} slides"
        print(msg)

        # Students: this is a ternary operator and lets us write an if/else
        # statement in one line. The reversal of syntax is the same as the
        # conversion from a for loop to a list comprehension.
        pdf = original_pdf if i < 0 else solutions_pdf
        page = pdf._get_page(abs(i))
        merged_pdf.add_page(page)

    with open(output_fp, "wb") as out_file:
        merged_pdf.write(out_file)

    return output_fp


def main():
    args = sys.argv
    assert 3 == len(args)
    section = args[1]
    original_fp = args[2]
    solutions_fp = [3]
    
    try:
        new_filepath = merge_pdfs(section, original_pdf, solutions_pdf)
        print("Written to:", new_file)
    except AssertionError as e:
        print("Your inputs throw an error")
        print("To use this file, try a command like this:")
        cmd = ("python exercise_3_merge_pds.py afternoon"
               " ~/Downloads/lecture-06.pdf"
               "  ~/Downloads/lecture-06-solutions.pdf")
        print(cmd)
        raise e


if '__main__' == __name__:
    doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)
    assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'
    main()
