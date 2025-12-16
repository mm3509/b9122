def invert_markdown(markdown):
    """
    >>> line0 = "# 15 oct 2025"
    >>> line1 = "notes"
    >>> line2 = "# 14 Oct 2025"
    >>> line3 = "other notes"
    >>> line4 = "## level 2 heading"
    >>> line5 = "yet other notes"
    >>> original1 = [line0, line1, line2, line3]
    >>> fixed1_str = invert_markdown("\\n".join(original1))
    >>> fixed1 = fixed1_str.split("\\n")
    >>> fixed1[0] == original1[2]
    True
    >>> fixed1[1] == original1[3]
    True
    >>> fixed1[2] == original1[0]
    True
    >>> fixed1[3] == original1[1]
    True
    >>> original2 = [line0, line2]
    >>> fixed2_str = invert_markdown("\\n".join(original2))
    >>> fixed2 = fixed2_str.split("\\n")
    >>> fixed2[0] == original2[1]
    True
    >>> fixed2[1] == original2[0]
    True
    >>> original3 = [line0, line1, line4, line5]
    >>> fixed3_str = invert_markdown("\\n".join(original3))
    >>> fixed3_str.split("\\n") == original3
    True
    >>> original4 = [line0, line1, line2, line3, line4, line5]
    >>> fixed4_str = invert_markdown("\\n".join(original4))
    >>> fixed4 = fixed4_str.split("\\n")
    >>> fixed4[:4] == original4[2:]
    True
    >>> fixed4[4:] == original4[:2]
    True
    >>> invert_markdown(123)
    Traceback (most recent call last):
    ...
    AssertionError
    """

    # TODO: add defensive programming.

    # TODO: implement the function.
    markdown = markdown.strip("\n")

    return
