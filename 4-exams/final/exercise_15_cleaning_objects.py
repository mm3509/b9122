def remove_number_0(arg):
    """
    >>> object1 = {"number": 0}
    >>> remove_number_0(object1)
    >>> object1
    {}
    >>> object2 = [{"number": 0, "key": "value"}, 2, 3]
    >>> remove_number_0(object2)
    >>> object2
    [{'key': 'value'}, 2, 3]
    >>> object3 = [{"number": 0, "key1": {"number": 0, "key2": "value2"}}]
    >>> object3.extend([2, 3, [{"number": 0, "key3": "value3"}]])
    >>> remove_number_0(object3)
    >>> object3
    [{'key1': {'key2': 'value2'}}, 2, 3, [{'key3': 'value3'}]]
    >>> object4 = [{"number": 1, "key": "value"}, 2, 3]
    >>> remove_number_0(object4)
    >>> object4
    [{'number': 1, 'key': 'value'}, 2, 3]
    >>> object5 = [1, 2, "abc", True]
    >>> remove_number_0(object5)
    >>> object5
    [1, 2, 'abc', True]
    >>> object6 = "abc"
    >>> remove_number_0(object6)
    >>> object6
    'abc'
    """

    # TODO: implement the function.

    return
