import nltk

from src.chunk_counters import (np_chunk_counter, vp_chunk_counter)


def pos_tag_text(word_tokenized_text):
    """
    Apply POS tagging to a list of
    word-tokenized sentences.
    """

    pos_tagged_text = []

    for sentence in word_tokenized_text:
        pos_tagged_text.append(nltk.pos_tag(sentence))

    return pos_tagged_text


def analyze_np_chunks(np_chunked_text):
    """
    Return the most common noun phrase chunks.
    """

    return np_chunk_counter(np_chunked_text)


def analyze_vp_chunks(vp_chunked_text):
    """
    Return the most common verb phrase chunks.
    """

    return vp_chunk_counter(vp_chunked_text)