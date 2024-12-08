#!/usr/bin/env python3
""" 
Module ADC day 3
"""
import re
import sys
data_filename = sys.argv[1]

def mul(a, b) -> int:
    return a * b


with open(data_filename, 'r', encoding="utf-8") as file:
    text_data = file.read()
    #search_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    SEARCH_PATTERN = r"(?:mul\(\d{1,3},\d{1,3}\))|(?:do\(\))|(?:don't\(\))"
    matches = re.findall(SEARCH_PATTERN,text_data)


    #print(sum(eval(match) for match in matches ))

    do_mul = True
    total = 0
    for match in matches:
        if "mul" in match and do_mul:
            total += eval(match)
        else:
            if "do()" in match:
                do_mul = True
            elif "don't()" in match:
                do_mul = False
    print(total)
