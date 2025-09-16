;; To set cursor to a thin bar instead of a rectangle, uncomment this.
;;(setq-default cursor-type 'bar)

;; Indentation of Python
(setq python-indent-offset 4)

;; Set the buffer-local variable `tab-width` at each new Python file
(add-hook 'python-mode-hook (lambda () (setq tab-width 4)))

(defun b9-args ()
  (interactive)
  (insert (combine-and-quote-strings '(
                                       ""
                                       "    args = sys.argv"
                                       "    assert 1 < len(args)"
                                       "    fp = args[1]"
                                       "    return"
                                       ) "\n")))


(defun b9-insert-python-boilerplate()
  (interactive)
  (insert (combine-and-quote-strings '(
                                       "#!/usr/local/bin/python3"
                                       ""
                                       "import doctest"
                                       "import glob"
                                       "import json"
                                       "import os"
                                       "import subprocess"
                                       "import sys"
                                       ""
                                       ) "\n"))
  (save-excursion
    (b9-main)))

(defun b9-main()
  (interactive)
  (insert (combine-and-quote-strings '(
                                       ""
                                       "def main():"
                                       "    pass"
                                       ""
                                       ""
                                       ""
                                       "if '__main__' == __name__:"
                                       "    doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)"
                                       "    assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'"
                                       "    main()") "\n")))



(defun b9-json ()
  (interactive)
  (insert "

    with open(fp, encoding='utf-8') as f:
        records = json.load(f)
    with open(fp, 'w+', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2, separators=(',', ':'))
"))

(defun b9-read ()
  (interactive)
  (insert "with open(")
  (save-excursion
    (insert ") as f:
    contents = f.read()
lines = re.split('\\r|\\n', contents)
")))

(defun b9-write ()
  (interactive)
  (insert "with open(fp, 'w+', encoding='utf-8') as f:
        f.write(\"\\n\".join())
"))



(defun b9-logistic()
  (interactive)
  (insert "import sklearn.linear_model
logistic = sklearn.linear_model.LogisticRegression(max_iter=int(1e5))
logistic_fit = logistic.fit(x_train, y_train)"))


(defun b9-datafilepath ()
  (interactive)
  (insert "import pathlib
import os

THIS_DIR = pathlib.Path(__file__).resolve().parent
DATA_FILEPATH = os.path.join(THIS_DIR, '')"))


(defun b9-csv ()
  (interactive)
  (insert "    with open(fp, mode ='r') as f:
        rows = csv.reader(f)
        for i, fields in enumerate(rows):
            uni = fields[2]
            answer = fields[9].lower()
"))

(defun b9-this-dir ()
  (interactive)
  (insert "import pathlib

THIS_DIR = pathlib.Path(__file__).resolve().parent
DATA_FILEPATH = os.path.join(THIS_DIR, \"data.csv\")"))

(defun b9-yfinance ()
  (interactive)
  (insert "import yfinance as yf
    ticker = yf.Ticker(\"^FTSE\")
    data = ticker.history(start=\"2000-12-31\")
    print(data[\"Close\"])"))

(defun b9-doctest-error ()
  (interactive)
  (insert "    Traceback (most recent call last):
    ...
    TypeError: ...
    ValueError: ...
"))

(defun b9-insert-doctests ()
  (interactive)
  (insert "
import doctest

    def compute_area(a, b):
    \"\"\"
    >>> compute_area(2, -1)
    Traceback (most recent call last):
        ...
        ValueError: arguments must be positive
    \"\"\"


if \"__main__\" == __name__:
    tests_failed, tests_run = doctest.testmod(optionflags=doctest.ELLIPSIS)
    if 0 < tests_run:
        assert 0 == tests_failed, 'Some doc-tests failed, exiting...'
        print('Your doc-tests pass, congratulations!')
    else:
        print('Unable to run doc-tests, please see Miguel!')"))


(defun b9-os-walk ()
  (interactive)
  (insert "
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            fp = os.path.join(root, name)
        for name in dirs:
            subdir = os.path.join(root, name)
"))
      

(defun b9-iterrows ()
  (interactive)
  (insert "
    for index, row in df.iterrows():

        print(row['colum_name'])"))

(defun b9-dirname-basename-extension ()
  (interactive)
  (insert "d = os.path.dirname(fp)
fn = os.path.basename(fp)
stem, extension = os.path.splitext(fn)
"))

