def change_bullet_style(document):
    """Convert bullet points in a document from '-' to '*'.
    Args:
        document: A string representing the document with bullet points.
    Returns:
        A string with bullet points converted from '-' to '*'.
    """
    document_arr = document.split('\n')
    converted_elements = map(convert_line, document_arr)

    results = "\n".join(converted_elements)
    
    return results


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
