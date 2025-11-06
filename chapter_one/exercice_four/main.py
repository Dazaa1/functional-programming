def get_median_font_size(font_sizes):
    """Calculates the median font size from a list of font sizes.
    Args:
        font_sizes (list): A list of font sizes (integers or floats).
    Returns:
        float or int or None: The median font size, or None if the list is empty.
    """
    if len(font_sizes) == 0:
        return None

    sorted_list = sorted(font_sizes)
    if len(sorted_list) % 2 != 0:
        value = sorted_list[len(sorted_list) // 2]
        return value

    else:
        value = sorted_list[(len(sorted_list) // 2) - 1]
        return value
