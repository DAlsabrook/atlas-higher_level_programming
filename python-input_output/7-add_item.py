#!/usr/bin/python3
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists("add_item.json"):
    obj = load_from_json_file("add_item.json")
else:
    obj = []
for arg in sys.argv[1:]:
    obj.append(arg)
save_to_json_file(obj, "add_item.json")
