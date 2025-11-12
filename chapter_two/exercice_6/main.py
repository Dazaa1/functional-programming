from functools import reduce


def join(doc_so_far, sentence):
    """Join two sentences with a period and a space.
    Args:
        doc_so_far: The current document string.
        sentence: The sentence to append.
    Returns:
        A string with the sentence appended to the document so far, separated by ". ".
    """
    return doc_so_far + ". " + sentence


def join_first_sentences(sentences, n):
    """Join the first n sentences from a list into a single string.
    Args:
        sentences: A list of sentences (strings).
        n: The number of sentences to join.
    Returns:
        A single string containing the first n sentences joined by ". "."
    """
    return reduce(join, sentences[:n]) + "." if n != 0 else ""
