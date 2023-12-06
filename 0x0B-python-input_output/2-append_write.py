#!/usr/bin/python3
"""function that appends a string at the end of a text file
and returns the number of characters added"""


def append_write(filename="", text=""):
    """append"""
    with open(filename, "a") as file:
        return file.write(text)
