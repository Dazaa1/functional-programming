def restore_documents(originals, backups):
    """Restores document names by combining originals and backups,
    converting them to uppercase and removing any that are purely numeric.
    Args:
        originals: A list of original document names.
        backups: A list of backup document names.
    Returns:
        A set of restored document names in uppercase without numeric-only names.
    """
    return set(filter(lambda el: not el.isdigit(), map(lambda el: el.upper(), originals + backups)))