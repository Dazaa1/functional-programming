def file_to_prompt(file, to_string):
    """Convert a file to a prompt string using the provided to_string function.
    
    Args:
        file: The file object to be converted.
        to_string: A function that takes a file object and returns its string representation.
    
    Returns:
        A string formatted as a code block containing the string representation of the file.
    """
    convert_to_string = to_string
    return f"```\n{convert_to_string(file)}\n```"