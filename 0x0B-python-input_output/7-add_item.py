#!/usr/bin/python3
"""script that adds all arguments to a Python list, then save them to a file"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
try:
    elements = load_from_json_file("add_item.json")
except FileNotFoundError:
    elements = []
elements.extend(sys.argv[1:])
save_to_json_file(elements, "add_item.json")
