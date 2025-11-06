def stylize_title(document):
    """Applies styling to the title of the document.
    Args:
        document (str): The document string with a title.

    Returns:
        str: The document with the styled title.
    """
    return add_border(center_title(document))


# Don't touch below this line


def center_title(document):
    width = 40
    title = document.split("\n")[0]
    centered_title = title.center(width)
    return document.replace(title, centered_title)


def add_border(document):
    title = document.split("\n")[0]
    border = "*" * len(title)
    return document.replace(title, title + "\n" + border)

