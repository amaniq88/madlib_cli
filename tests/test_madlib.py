import pytest
from madlib_cli.madlib import read_template, parse_template , merge


def test_read_template_returns_stripped_string():
    actual = read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


#@pytest.mark.skip("pending")
def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


#@pytest.mark.skip("pending")
def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


#@pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)


def test_read_testData():
    actual = read_template("assets/testData.txt")
    expected = "I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s."
    assert actual == expected

def test_parse_testData():
    actual_stripped, actual_parts = parse_template(
        "I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s."
    )
    expected_stripped = "I the {} and {} {} have {}{}'s."
    expected_parts = ("Adjective", "Adjective", "A First Name", "Past Tense Verb","A First Name")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts

def test_merge_testData():
    actual = merge("I the {} and {} {} have {}{}'s.", ("dark", "stormy", "night", "Amani", "Ali"))
    expected = "I the dark and stormy night have AmaniAli's."
    assert actual == expected

