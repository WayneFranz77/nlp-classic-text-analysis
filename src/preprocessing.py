from pathlib import Path

from nltk.tokenize import (PunktSentenceTokenizer, word_tokenize)


def load_text(file_path: str) -> str:
    """Load text file and convert to lowercase."""

    return Path(file_path).read_text(encoding="utf-8").lower()


def word_sentence_tokenize(text: str) -> list[list[str]]:
    """Tokenize text into sentences and words."""

    sentence_tokenizer = PunktSentenceTokenizer(text)

    sentence_tokenized = sentence_tokenizer.tokenize(text)

    word_tokenized = []

    for sentence in sentence_tokenized:
        word_tokenized.append(word_tokenize(sentence))

    return word_tokenized