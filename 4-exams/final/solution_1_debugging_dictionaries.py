UNI_TO_PROGRAM = {
    "pea21": "MSAFA",
    "yb26": "MSAFA",
    "fb27": "MSAFA",
    "hc36": "MSAFA",
    "rc38": "MSAFA",
    "rc38": "MSAFA",
    "yc36": "MSAFA",
    "tc33": "MSAFA",
    "hc35": "MSAFA",
    "epc21": "MSAFA",
    "oad21": "MSAFA",
    "xd23": "MSAFA",
    "jd42": "MSAFA",
    "zf23": "MSAFA",
    "kg32": "MSAFA",
    "hh28": "MSAFA",
    "yh37": "MSAFA",
    "yj25": "MSAFA",
    "yk29": "MSAFA",
    "bl31": "MSAFA",
    "ml51": "MSAFA",
    "zl33": "MSAFA",
    "sl58": "MSAFA",
    "hl39": "MSAFA",
    "cl45": "MSAFA",
    "yl60": "MSAFA",
    "ggm21": "MSAFA",
    "dcm21": "MSAFA",
    "zn22": "MSAFA",
    "mn33": "MSAFA",
    "zp22": "MSAFA",
    "ds43": "MSAFA",
    "mcv21": "MSAFA",
    "yw43": "MSAFA",
    "mm35": "MSAFA",
    "dw32": "MSAFA",
    "cw36": "MSAFA",
    "gw25": "MSAFA",
    "xw28": "MSAFA",
    "xx24": "MSAFA",
    "yx29": "MSAFA",
    "yx30": "MSAFA",
    "jx26": "MSAFA",
    "yy35": "MSAFA",
    "jy34": "MSAFA",
    "yy33": "MSAFA",
    "cy28": "MSAFA",
    "qy23": "MSAFA",
    "sy33": "MSAFA",
    "yz52": "MSAFA",
    "hz30": "MSAFA",
    "yz51": "MSAFA",
    "cz28": "MSAFA",
    "yz52": "MSAFA",
    "hz30": "MSAFA",
    "oa24": "MSFE",
    "sb52": "MSFE",
    "pb29": "MSM",
    "dfb21": "MSFE",
    "wc29": "MSFE",
    "wd24": "MSFE",
    "yf27": "MSFE",
    "kf28": "MSFE",
    "yf27": "MSFE",
    "yf27": "MSFE",
    "xg24": "MSFE",
    "zg24": "MSAFA",
    "zgao": "MSAFA",
    "hg27": "MSFE",
    "jh50": "MSFE",
    "yh39": "MSFE",
    "mh46": "MSFE",
    "jh51": "MSFE",
    "sh47": "MSFE",
    "yh39": "MSFE",
    "tl34": "MSFE",
    "kl37": "MSFE",
    "jm61": "MSFE",
    "mlm23": "MSFE",
    "xr21": "MSFE",
    "ys40": "MSFE",

    # The bug was here: keys are unique, so repeating this key overwrote the
    # previous definition. This is one example where the style check would have
    # warned you of repeated keys and avoided a bug.

    # "mm35": "MSFE",
    "ts37": "MSFE",
    "zs27": "MSFE",
    "ss76": "MSFE",
    "xs26": "MSFE",
    "xt23": "MSFE",
    "jt36": "MSFE",
    "yw45": "MSFE",
    "rw31": "MSFE",
    "tw31": "MSFE",
    "zx25": "MSFE",
    "yy36": "MSFE",
    "zy27": "MSFE",
    "ky26": "MSFE",
    "sy28": "MSFE",
    "rz27": "MSFE",
    "xz30": "MSFE",
    "wz27": "MSFE",
    "rz27": "MSFE",
    "hz30": "MSFE",
    "xz34": "MSFE",
    "hz30": "MSFE",
}


def __find_first_digit_index_in_string_helper(uni):
    """
    >>> __find_first_digit_index_in_string_helper("mm35")
    2
    >>> __find_first_digit_index_in_string_helper("abcd35")
    4
    """

    index = 0
    for c in uni:
        if ord("0") <= ord(c) <= ord("9"):
            break
        index += 1

    return index


def uni_to_program(uni):
    """
    >>> uni_to_program("yl60")
    'MSAFA'
    >>> uni_to_program("YL60")
    'MSAFA'
    >>> uni_to_program("xr21")
    'MSFE'
    >>> uni_to_program("XR21")
    'MSFE'
    >>> uni_to_program("mm35")
    'MSAFA'
    >>> uni_to_program("MM35")
    'MSAFA'
    >>> None is uni_to_program("abcd1234")
    True
    >>> uni_to_program(123)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> uni_to_program("mm3")
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> uni_to_program("m35")
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> uni_to_program("uni-with-invalid-characters")
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    assert isinstance(uni, str)
    uni = uni.lower()
    assert 4 <= len(uni)
    index_of_first_digit = __find_first_digit_index_in_string_helper(uni)
    part1 = uni[:index_of_first_digit]
    part2 = uni[index_of_first_digit:]

    assert 2 <= len(part1)
    assert 2 <= len(part2)

    assert all([ord("a") <= ord(c) <= ord("z") for c in part1])
    assert all([ord("0") <= ord(c) <= ord("9") for c in part2])

    return UNI_TO_PROGRAM.get(uni)
