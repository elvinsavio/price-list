import re


def clean_string(input_string: str) -> str:
    """
    Takes a string from the user and sanitizes it so search

    Args:
        a (str): Input

    Returns:
        str: Sanitized string
    """
    return re.sub(r"[^a-zA-Z0-9 ]", "", input_string).replace(" ", "-")


def remove_hyphen(input_string: str) -> str:
    """
    Takes a sanitized string and formats it to be sent to the ui

    Args:
        a (str): Input

    Returns:
        str: Formatted string
    """
    return input_string.replace("-", " ")
