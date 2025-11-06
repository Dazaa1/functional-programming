def choose_parser(file_extension):
    """Chooses the appropriate parser based on the file extension.
    Args:
        file_extension (str): The file extension of the document.
    Returns:
        str: The chosen parser ("markdown" or "plaintext").
    """
    return "markdown" if file_extension.lower() in ("markdown", "md") else "plaintext"
