from collections import Counter


def np_chunk_counter(chunked_sentences, top_n=30):
    chunks = []

    for sentence in chunked_sentences:
        for subtree in sentence.subtrees(
            filter=lambda t: t.label() == "NP"
        ):
            chunks.append(tuple(subtree))

    return Counter(chunks).most_common(top_n)


def vp_chunk_counter(chunked_sentences, top_n=30):
    chunks = []

    for sentence in chunked_sentences:
        for subtree in sentence.subtrees(
            filter=lambda t: t.label() == "VP"
        ):
            chunks.append(tuple(subtree))

    return Counter(chunks).most_common(top_n)