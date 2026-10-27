from collections import Counter


def character_counter(chunked_sentences):

    characters = []

    for sentence in chunked_sentences:

        for subtree in sentence.subtrees():

            if subtree.label() == "NAME":

                name = " ".join(
                    word
                    for word, tag in subtree.leaves()
                )

                characters.append(name)

    return Counter(characters).most_common(20)