#!/usr/bin/python3
def text_indentation(text):
    """
    Check if text is a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    """
    Initialize the result string
    """
    result = ("")

    """
    Process each character in the text
    """
    for char in text:
        """
        Add the character to the result
        """
        result += char

        """
        Check if the character is '.', '?', or ':'
        """
        if char in ('.', '?', ':'):
            """
            Add two new lines after the character
            """
            result += '\n\n'

    """
    Print the result
    """
    print(result)

