#!/usr/bin/python3
"""
Module to create obj from json file
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

obj = load_from_json_file("add_item.json")
print("loaded")
for arg in sys.argv:
    obj.append(arg)
    print(f"Arg: {arg}")
save_to_json_file(obj, "add_item.json")
print("saved")
