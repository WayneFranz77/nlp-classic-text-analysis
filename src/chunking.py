import nltk


def create_np_parser() -> nltk.RegexpParser:
    """
    Create a noun phrase parser.

    NP:
    Optional determiner (DT)
    Zero or more adjectives (JJ)
    Noun (NN)
    """

    np_chunk_grammar = r"""NP: {<DT>?<JJ.*>*<NN.*>+}"""

    return nltk.RegexpParser(np_chunk_grammar)


def create_vp_parser() -> nltk.RegexpParser:
    """
    Create a verb phrase parser.

    VP:
    Noun phrase
    Verb
    Optional adverb
    """

    vp_chunk_grammar = r"""VP: {<VB.*><RB.*>*}"""

    return nltk.RegexpParser(vp_chunk_grammar)

def chunk_sentences(
    pos_tagged_text,
    parser: nltk.RegexpParser):
    """
    Apply a parser to a collection of
    POS-tagged sentences.
    """

    chunked_text = []

    for sentence in pos_tagged_text:
        chunked_text.append(parser.parse(sentence))

    return chunked_text

def create_name_parser() -> nltk.RegexpParser:

    grammar = r"""NAME: {<NNP>+}"""

    return nltk.RegexpParser(grammar)