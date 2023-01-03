#!/usr/bin/python3
"""
A module for implimentation of text indentation
"""


def text_indentation(text):
    """A function that rints a text with 2 new lines after each of these characters: ., ? and :
    Args: text: a text to be indented
    Return: Nothing
    Raises: TypeError: if the text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    print(text.strip(), end='')
