def verify_argument(alist):

    assert isinstance(alist, list)
    assert all([isinstance(element, int) for element in alist])


def find_triplets(alist):
    """
    >>> find_triplets([-5, 3, 9, 4])
    21
    >>> find_triplets(123)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> find_triplets([1, "2", 3])
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    verify_argument(alist)

    n = len(alist)
    maximum = sum(alist)

    for i in range(n):
        for j in range(i, n + 1):
            for k in range(j, n + 1):
                value = (sum(alist[:i])
                         - sum(alist[i:j])
                         + sum(alist[j:k])
                         - sum(alist[k:]))

                if value >= maximum:
                    maximum = value

    return maximum


def find_triplets_medium(alist):
    # Here is one way to make this faster, even though it's not enough.

    # The optimal indices will always be at sign flips, when one element is
    # positive and the other is negative or one element is negative and the
    # other is positive (otherwise, the gross value increases by incrementing
    # the index, lengthening a running sum with a plus sign in front, or
    # lengthening a negative sum with a minus sign in front). So restrict the
    # search to those indices.

    n = len(alist)
    sign_flips = []

    for i in range(1, n):
        if alist[i] * alist[i - 1] <= 0:
            sign_flips.append(i)

    markers = [0] + sign_flips + [n]

    m = len(markers)
    maximum = sum(alist)
    for i_marker in range(m):
        i = markers[i_marker]

        for j_marker in range(i_marker, m):
            j = markers[j_marker]

            for k_marker in range(j_marker, m):
                k = markers[k_marker]

                value = (sum(alist[:i])
                         - sum(alist[i:j])
                         + sum(alist[j:k])
                         - sum(alist[k:]))

                if value > maximum:
                    maximum = value

    return maximum


def find_triplets_fast(alist):
    """
    >>> find_triplets_fast([-5, 3, 9, 4])
    21
    >>> find_triplets_fast(123)
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(alist, list)
    assert all(isinstance(x, int) for x in alist)

    n = len(alist)

    prefix = [0] * (n + 1)
    for idx in range(n):
        prefix[idx + 1] = prefix[idx] + alist[idx]

    best_left = [0] * (n + 1)
    best_left[0] = prefix[0]
    for j in range(1, n + 1):
        best_left[j] = max(best_left[j - 1], prefix[j])

    best_right = [0] * (n + 1)
    best_right[n] = prefix[n]
    for j in range(n - 1, -1, -1):
        best_right[j] = max(best_right[j + 1], prefix[j])

    max_f = None
    for j in range(n + 1):
        value = best_left[j] - prefix[j] + best_right[j]
        if max_f is None or value > max_f:
            max_f = value

    maximum = 2 * max_f - prefix[n]
    return maximum
