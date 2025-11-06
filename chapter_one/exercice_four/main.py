def get_median_font_size(font_sizes):
    """Calculates the median font size from a list of font sizes.
    Args:
        font_sizes (list): A list of font sizes (integers or floats).
    Returns:
        float or int or None: The median font size, or None if the list is empty.
    """
    if len(font_sizes) == 0:
        return None
    return sorted(font_sizes)[(len(font_sizes) - 1) // 2]

