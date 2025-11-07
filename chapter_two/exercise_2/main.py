def file_type_getter(file_extension_tuples):
    """Create a function that maps file extensions to their corresponding file types.
    
    Args:
        file_extension_tuples: A list of tuples where each tuple contains a file type and a
            list of associated file extensions.
    Returns:
        A function that takes a file extension as input and returns the corresponding file type.
    """

    file_extension = {}
    for element in file_extension_tuples:
        for extension in element[1]:
            file_extension[extension] = element[0]

    return lambda file_ex: file_extension.get(file_ex, "Unknown")
