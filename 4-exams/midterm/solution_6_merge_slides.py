def merge_solutions_into_slides(original, solutions, additional_pages):
    """
    >>> merge_solutions_into_slides(3, 4, [3])
    [-1, -2, 3, -3]
    >>> merge_solutions_into_slides(3, 5, [3, 4])
    [-1, -2, 3, 4, -3]
    >>> merge_solutions_into_slides(1.5, 1, [])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> merge_solutions_into_slides(1, "1", [])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> merge_solutions_into_slides(1, 0, {})
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> merge_solutions_into_slides(1, 0, [])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> merge_solutions_into_slides(1, 3, [1, "cd"])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> merge_solutions_into_slides(1, 2, [4])
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> merge_solutions_into_slides(1, 3, [4, 4])
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    for arg in [original, solutions]:
        assert isinstance(arg, int)
        assert arg >= 1
    assert isinstance(additional_pages, list)

    # Students: because I trim solutions slides at the point where we end, I
    # disable this check.

    # assert solutions == original + len(additional_pages)

    assert all([isinstance(p, int) for p in additional_pages])
    assert all([1 <= p <= solutions for p in additional_pages])
    assert len(set(additional_pages)) == len(additional_pages)

    merged = []
    current_page_in_original = 1
    for solutions_page in range(1, solutions + 1):
        if solutions_page in additional_pages:
            merged.append(solutions_page)
            continue

        merged.append(-current_page_in_original)
        current_page_in_original += 1

    return merged
