def add_prefix(document, documents):
    """Adds a numerical prefix to the document based on its position in the documents tuple.
    Args:
        document (str): The document string to which the prefix will be added.
        documents (tuple): A tuple of document strings.
    Returns:
        tuple: A new tuple of documents with the prefixed document added.
    """
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    # (new_doc,) creates a new tuple with the value of new_doc
    document_final = documents + (new_doc,)
    return document_final
