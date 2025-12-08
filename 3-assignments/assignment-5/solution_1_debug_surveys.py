import datetime


PROGRESS_KEY = "progress"


def add_to_survey(survey, question, answer):
    """
    >>> new_survey = add_to_survey({}, "q1", "a1")
    >>> new_survey["q1"]
    'a1'
    >>> new_survey["progress"]  # doctest: +ELLIPSIS
    ['Answered q1 on...']
    """

    assert isinstance(survey, dict)
    for arg in [question, answer]:
        assert isinstance(arg, str)

    survey[question] = answer

    # Students: this is how you can get the current time:
    now = datetime.datetime.now()

    # And this is how you can convert it to a string with the ISO format:
    now_str = now.isoformat()

    completion = f"Answered {question} on {now_str}"

    # Students: .append() works-in place and returns nothing, so the exercise
    # file set the value of that key to None. To append to the previous values,
    # you can do it this way:
    progress = survey.get(PROGRESS_KEY, [])
    progress.append(completion)
    survey[PROGRESS_KEY] = progress

    return survey
