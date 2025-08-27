# Appendix: grading / method of evaluation

| **Weight** | **Component**                                   |
|------------|-------------------------------------------------|
| 15%        | class attendance                                |
| 5%         | online polls                                    |
| 5%         | online quizzes                                  |
| 5%         | end-of-lecture submissions                      |
| 10%        | class participation                             |
| 20%        | 5 assignments                                   |
|            | (5% each, lowest grade dropped)                 |
| 15%        | midterm exam                                    |
| 25%        | final exam                                      |


## Conversion to a letter grade

To convert from a numeric grade to a letter grade, I will use a variation of k-means clustering. The code searches for thresholds of letter grades that minimize the variance within each cluster, while maintaining the spacing between letters (A+, A, A-, B+, B, B-, C, D, E, F) roughly constant. We may cover this code in the lecture on k-means, clustering and basic optimization.

All items are graded out of 140 points. The rest of this document covers each item in detail.

## Class attendance

The grade for in-person attendance is proportional to in-person attendance, up to a maximum of 18 half-lectures. The first lecture, before the end of add-drop, does not require attendance. See before regarding the 4 freebie half-lectures. The function to grade class attendance is:

``` python
def normalize(grade):
    return 140 * min(1, grade)

def grade_attendance(half_lectures):
    return normalize(len(half_lectures) / 18)
```

## Online polls

During lecture, I regularly ask for feedback with online polls on PollEverywhere.com. You must register for an account and you **must use your Columbia email** (I discard all non-Columbia answers when computing the grade). The function to grade online polls is:

``` python
MAX_ONLINE_GRADE = 85  # Capped at 85%.

def grade_online_polls(polleverywhere):
    return normalize(polleverywhere["participation"] / MAX_ONLINE_GRADE)
```

## Online quizzes

Some lectures have an online quiz at the beginning to review the material from the previous lecture or lectures. The difference between an online poll and an online quiz is:

- online polls don't have a right answer: you earn points by simply participating;

- online quizzes have a right answer: you earn points by answering correctly.

Regular quizzes ensure that you stay on top of the material (because studying for it just before the exam is a recipe for disaster). The function to grade online quizzes is:

``` python
def grade_online_quizzes(polleverywhere):
    return normalize(polleverywhere["grade"] / MAX_ONLINE_GRADE)
```

## End-of-lecture submissions

Most lectures are hands-on and require you to run code along with me. You must submit your Python code in a text file or Jupyter notebook, or your shell logs or other screenshots, on the Gradescope assignment called "end-of-lecture submissions". The Autograder will give your submission a grade at the end of lecture day; but I reserve the right to inspect the submission and revert the grade (for example, in case two students cheat and submit the same document).

The function to grade your end-of-lecture submissions is:

``` python
def grade_end_of_lecture_submissions(submission_grades):
    return normalize(polleverywhere["grade"] / MAX_ONLINE_GRADE)
```

## Class participation

I grade class participation on a curve, with positive and negative items, rescaled to 0-70 for negative items and to 70-140 for positive items. In the baseline case where you demonstrate courtesy and respect (no negative participation) but also don't contribute or ask any questions (no positive participation), you will get 70 points.

Most reasons to gain and lose points revolve around questions and classroom etiquette. I want and expect you to ask questions, and I also expect you to be courteous when doing so. For example, I expect you to raise your hand to ask a question, or to wait until I solicit questions; this prevents interrupting the flow of the lecture.

Reasons to gain points:

- answering a question when I call on you: 1

- sharing or commenting from your experience: 1

- providing negative/constructive feedback to improve the lecture material, my teaching, or my grading: 1

- asking questions in class: 2

- answering a general question in class: 3

- proposing a good question for a guest lecturer: 3

Reasons to lose points:

- leaving class after attendance: 0 or 1 (0 at the start of term; it will only go to 1 if I notice too many people walking in and out and it disrupts the class, and I will warn you ahead of time)

- being distracted in class and using your computer to browser other websites: 1

- eating in class: 1

- using a cell phone in class: 1

- interrupting, e.g. by asking an unsolicited question: 1

- requiring frequent reminders to update color post-its during hands-on activities: 1

- talking with neighbor after a warning by me: 1

- cell phone ringing in class, or other disruptions: 3

- answering a phone call in class: 5

- being distracted during intervention by a guest lecturer: 5

- openly ignoring or dismissing an explicit request I made: 5

- monopolizing class time twice by asking too many questions, or redundant questions: 5 ("Monopolizing" means taking over 5 minutes during a lecture. I will flag that to you personally and individually. You will only lose points if you ignore that warning. This ensures other students feel permission to ask questions too.)

The function to grade class participation is:

``` python
def grade_class_participation(uni, participation_list):

    all_unis = [t[0] for t in participation_list]
    negative = dict.fromkeys(all_unis, 0)
    positive = dict.fromkeys(all_unis, 0)
    
    for uni, points in participation_list:
        if points < 0:
            negative[uni] += points
        else:
            positive[uni] += points
    rescaling_positive = max(positive)
    rescaling_negative = min(negative)
    
    return MAX_POINTS * (1 / 2
                         + positive[uni] / max(positive)
                         - negative[uni] / min(negative))
```

## Assignments

I release assignments after after a lecture; they are due on the Tuesday around 10 days later, so you have two weekends to complete them. I drop the lowest grade among the 5 assignments.

The grading for assignments and exams is the same: see below for the grading rubric.

## Exams

Exams are in-person and last 3 hours. We will have a midterm and a final exam. See below for the grading rubric.

One week before the exam, I will send you a study guide so you can review the material and be prepared for the exam.

## Assessment grading rubric and Autograder

This course uses an "Autograder" on Gradescope: you write code to complete the assignments, and I write code that gauges the quality of your code.

For assignments, you have three submissions per day and Autograder will give you an indication of your grade, so you can improve and get maximum points. The earlier you start on the assignments, the more submissions and opportunities for improvement you'll have.

Any question marked as "bonus" increases your grade to the maximum of 140 in the particular assessment and do not carry over to other assessments. That is, bonus questions serve as insurance within an assessment (in case you lost points on another question) but not across assessments (in case you lost points on another assignment).

This section details the grading standards that will apply by the end of the term: we will build towards these standards gradually. For example, in the first assignment, your code can have up to 50% of lines that are a comment, but by the end of term, your comments must be under 20% for full credit.

The grade for each assignment and exam is the weighted sum: the sum of points weighted by the percentage of each criterion. This sum is across automated and manual grading (the sum of both weights equals 100%). In the case where one criterion does not apply, the weights are rescaled to sum to 100%. If this is confusing, please do not worry about it: Autograder will always show you a grade out of 140 points.

Automated grading can be overridden manually. For example, your code passes the doc-tests because you tested specifically for those arguments. We will remove all points in the relevant rubrics. Your grade decreases.

I expect your code to run "out-of-the-box"

Please check our GitHub page, at `1 admin/grading standards` for examples and guidance on each grading criterion, and the pages at `1 admin/guides` for a guide to GitHub and Gradescope.

### Automated grading: 65%

- **Delivery** (0%): your code should run "out-of-the-box", , i.e. you submit it on Gradescope and it runs without intervention from the TAs or me. If you have trouble with this, please come to office hours. If your submission to an assignment or exam fails to run out-of-the-box, we will activate the previous submission with the highest automatic grade. If there is no such submission, your code assessment will earn a zero overall grade.

- **Doc-tests and test-driven development** (10%): for full credit, the code has the required number of doc-tests and passes all of them; otherwise, partial credit is proportional to the number of doc-tests it passes.

- **Defensive programming** (10%): for full credit, the code raises errors on all edge and corner cases (beyond test and corner cases supplied, and if required in the assignment). Note that this criterion is hidden until the due date: you will have to think for yourself which edge cases could be present, and anticipate for them ahead of receiving your grade.

- **Results** (25%): for full credit, the code does what it is supposed to do and provides the right output for test input; otherwise, partial credit is proportional to the number of test cases it passes.

- **Speed** (5%): for full credit, the code runs faster than the required time (equal to 2x the running time of my code); otherwise, partial credit is proportional to the interpolation between the required time and a timeout (equal to 5 times the running time of my code).

- **Comments** (5%): the share of comments, ignoring those providing attribution of code origin, is below the suggested maximum share.

- **Style** (10%): for full credit, the code follows the style guidelines for the assignment, with no errors flagged on Gradescope; otherwise, partial credit is proportional to 10 minus the number of style errors.

### Manual grading: 35%

- **Refactoring, conciseness, and DRY** ("Don't Repeat Yourself") (15%): for full credit, the code is well-refactored and DRY ("Don't Repeat Yourself"), no functionality is repeated twice, all functions are under 20 lines (after doc-tests and defensive programming tests).

- **Readability** (other than rubric above on refactoring) (15%): for full credit, the code is easy to read and understand; variable, function and object names are appropriate and convey meaning; functions are clear in what they do; they follow the "happy path". The code is so clear in what it does that there are obviously no bugs.

- **Comments** (5%): Comments are used wisely, to convey meaning to humans (e.g., to fix bugs, to add notes to yourself later). For full credit, all comments follow the StackOverflow guidelines.

