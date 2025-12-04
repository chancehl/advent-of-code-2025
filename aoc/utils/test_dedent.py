from .dedent import dedent


def test_dedent_with_multiline_string():
    input = """
        This string
        has several
        newlines between words
    """

    assert dedent(input) == "This string\nhas several\nnewlines between words"


def test_dedent_with_empty_string():
    assert dedent("") == ""


def test_dedent_with_single_line_string():
    assert dedent("hello world") == "hello world"


def test_dedent_with_multiline_string_with_single_line():
    input = """
        single line
    """

    assert dedent(input) == "single line"
