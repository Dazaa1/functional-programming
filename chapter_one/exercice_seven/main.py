def hex_to_rgb(hex_color):
    """Converts a hexadecimal color string to its RGB components.
    Args:
        hex_color (str): A hexadecimal color string (e.g., "FFA07A").
    Returns:
        tuple: A tuple containing the RGB components as integers.
    """
    if not is_hexadecimal(hex_color) or len(hex_color) != 6:
        raise Exception("not a hex color string")
    r = int(hex_color[:2], base=16)
    g = int(hex_color[2:4], base=16)
    b = int(hex_color[4:], base=16)

    return r, g, b


# Don't edit below this line


def is_hexadecimal(hex_string):
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False
