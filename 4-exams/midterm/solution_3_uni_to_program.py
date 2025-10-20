import string


VALID_CHARACTERS = string.ascii_letters + string.digits + ".@_"


def validate_email_and_get_username(email):
    assert isinstance(email, str)
    assert all([c in VALID_CHARACTERS for c in email])
    pieces = email.split("@")
    assert 2 == len(pieces)

    username = pieces[0]
    assert username != ""
    assert username[0] in string.ascii_letters

    assert any([c in string.ascii_letters for c in username[1:]])

    # Students: alternatively, you could write this last condition as:

    # assert 1 <= sum(ch.isalpha() for ch in username)

    # Students: another alternative for the last condition, with a for loop:

    # num_letters = 0
    # for c in username:
    #     if c in string.ascii_letters:
    #         num_letters += 1
    #
    # assert 2 <= num_letters

    return username


def uni_to_program(email, uni_dict):
    """
    >>> uni_dict = {'uni1': 'MSAFA', 'uni2': 'MSFE', 'uni3': 'MSFE'}
    >>> uni_to_program('uni1@columbia.edu', uni_dict)
    'MSAFA'
    >>> uni_to_program('Uni2@gsb.columbia.edu', uni_dict)
    'MSFE'
    >>> uni_to_program('uni3@engineering.columbia.edu', uni_dict)
    'MSFE'
    >>> uni_to_program('uni4@columbia.edu', uni_dict)
    'both'
    >>> uni_to_program('uni1', [])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> uni_to_program('uni1@columbia.edu', {})
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> uni_to_program(123, {"uni1": "MSAFA"})
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> uni_to_program("@columbia.edu", {"uni1": "MSAFA"})
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> uni_to_program("ça@columbia.edu", {"uni1": "MSAFA"})
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> uni_to_program("invalid/@columbia.edu", {"uni1": "MSAFA"})
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> uni_to_program("invalid@gsb@columbia.edu", {"uni1": "MSAFA"})
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> uni_to_program("3mm@columbia.edu", {"uni1": "MSAFA"})
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> uni_to_program("m@gsb.columbia.edu", {"uni1": "MSAFA"})
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> uni_to_program('uni1', {"uni1": "MSAFA"})
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(uni_dict, dict)
    assert 0 < len(uni_dict.keys())  # Alternatively: assert uni_dict

    username = validate_email_and_get_username(email)

    return uni_dict.get(username.lower(), "both")
