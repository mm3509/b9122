SEARCH_PREFIXES_TO_GET_TERMS = [
    "https://www.ebay.fr/sch/i.html?_nkw=",
    "https://www.ebay.co.uk/sch/i.html?_nkw=",
    "https://www.ebay.com/sch/i.html?_nkw=",
]

SEARCH_TERMS_END = "&"
SEARCH_TERMS_DELIMITER = "+"


def get_search_terms(url):
    """
    >>> get_search_terms("https://www.ebay.com/sch/i.html?_nkw=toy+parrot&p=5")
    ['toy', 'parrot']
    >>> get_search_terms("https://www.ebay.fr/sch/i.html?_nkw=toy+parrot&a=0")
    ['toy', 'parrot']
    >>> get_search_terms("https://www.ebay.fr/sch/i.html?_nkw=some+book&x23=0")
    ['some', 'book']
    >>> get_search_terms("https://www.ebay.co.uk/sch/i.html?_nkw=tale+cities")
    ['tale', 'cities']
    >>> get_search_terms("https://www.ebay.com/sch/i.html?_nkw=something&a=n")
    ['something']
    >>> a_long_url = "https://www.ebay.com/sch/i.html?_nkw=A+practical+guide"
    >>> get_search_terms(a_long_url)
    ['a', 'practical', 'guide']
    >>> get_search_terms("https://google.com")
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    # TODO: add defensive programming.

    # TODO: implement the function.

    return
