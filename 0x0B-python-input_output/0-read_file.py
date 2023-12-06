#!/usr/bin/python3
"""function that reads a text file and prints it"""


def read_file(filename=""):
    """print"""
    with open(filename) as file:
        print(file.read().strip())
