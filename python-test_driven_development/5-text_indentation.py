#!/usr/bin/python3
"""Module of text indentation method"""


def text_indentation(text):
    """Print a text with two new lines after special characters '.', '?', ':':

    Args:
        text: content to print

    Raises:
        TypeError: text is not a string

    Returns:
        The text without space at the beginning or the end of each new lines.
        The function prints the text with 2 new lines after special characters.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char_spec = ['.', '?', ':']
    new_line = True
    for index in text:
        if new_line and index == ' ':
            continue  # Skip leading spaces at the beginning of new lines
        elif index == '\n':
            new_line = True  # Set flag for new line
        elif index in char_spec:
            print(index + "\n\n", end='')
            new_line = True  # Set flag for new line after special character
        else:
            print(f"{index}", end='')
            new_line = False  # Reset flag for new line
