import pytest
from project import determine_status, grading, start_or_exit


def test_determine_status():
    assert determine_status("A") == "Passed 🥳"
    assert determine_status("B") == "Passed 🥳"
    assert determine_status("C") == "Passed 🥳"
    assert determine_status("D") == "Passed 🥳"
    assert determine_status("E") == "Failed 😔"
    assert determine_status("F") == "Failed 😔"


def test_grading():
    assert grading(1) == "F"
    assert grading(100) == "A"
    assert grading(52) == "E"
    assert grading(70) == "C"
    assert grading(65) == "D"


def test_start_or_exit():
    assert start_or_exit("start") is True
    assert start_or_exit("restart") is True
    assert start_or_exit("play") is True
    assert start_or_exit("continue") is True
    assert start_or_exit("exit") is False
    assert start_or_exit("close") is False
    assert start_or_exit("end") is False
    assert start_or_exit("stop") is False

    with pytest.raises(ValueError):
        start_or_exit("yes")
        start_or_exit("no")
        start_or_exit("")
