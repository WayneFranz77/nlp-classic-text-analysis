# tests/test_preprocessing.py

from src.preprocessing import load_text


def test_load_text():

    text = load_text(
        "data/raw/dorian_gray.txt"
    )

    assert isinstance(text, str)
    assert len(text) > 0