def word_count_memo(document, memos):
    """Returns the word count of a document, using memoization to avoid redundant calculations.
    Args:
        document (str): The document whose words are to be counted.
        memos (dict): A dictionary storing previously computed word counts for documents.
    Returns:
        tuple: A tuple containing the word count of the document and the updated memos dictionary.
    """
    memos_copy = memos.copy()
    if document in memos_copy.keys():
        return memos_copy[document], memos_copy

    word_count_var = word_count(document)
    memos_copy[document] = word_count_var
    return word_count_var, memos_copy


# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count