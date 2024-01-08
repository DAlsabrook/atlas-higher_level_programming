#!/usr/bin/python3

def common_elements(set_1, set_2):
    if set_1 is None or not set_1 or set_2 is None or not set_2:
        return None
    common_elements = {}
    for element in set_1:
        for item in set_2:
            if element == item:
                common_elements.append(element)
    return common_elements

