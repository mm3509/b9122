# Help on the code in this section

## merging PDFs

Use case: you want to merge the PDF slides from the solutions I publish after class to the slides you annotated during class.

This file uses the solutions to the midterm question on slides.

For example, if you are in the morning section and have the slides saved at `~/Downloads/B9122`, running this shell command should save and open a new PDF file with the merged slides:

``` bash
python merge_pdfs.py morning ~/Downloads/lecture-06.pdf ~/Downloads/lecture-06-solutions.pdf
```

If you are in the afternoon section, this is the equivalent command:

``` bash
python merge_pdfs.py afternoon ~/Downloads/lecture-06.pdf ~/Downloads/lecture-06-solutions.pdf
```

If you see this error:

```
ModuleNotFoundError: No module named 'solution_6_merge_slides'
```

you need to update the repository on your computer with these commands:

``` bash
cd $HOME/b9122
git pull
```

