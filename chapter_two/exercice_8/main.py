valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pair_document_with_format(doc_names, doc_formats):
    """Pairs document names with their formats and filters out invalid formats.
    Args:
        doc_names: A list of document names.
        doc_formats: A list of document formats corresponding to the document names.
    Returns:
        A list of tuples containing valid document names and their formats.
    """
    # we did association
    # then we filtered
    return list(filter(lambda doc: doc[1] in valid_formats, list(zip(doc_names, doc_formats))))
    # finally we extracted names
    # return list(map(lambda doc: doc[0], filtered_docs)) --- IGNORE ---