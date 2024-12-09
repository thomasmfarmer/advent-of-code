#!/usr/bin/env python3
""" 
Module ADC day 4
"""

import sys
import numpy as np
#data_filename = "2024/04-Ceres-Search/Ceres-Search-Test-Data.txt"
data_filename = sys.argv[1]

with open(data_filename, 'r', encoding="utf-8") as file:
    lines = file.readlines()

rows = len(lines)
cols = len(lines[0].strip())

puzzle = np.empty((rows, cols), dtype=str)
search_word = np.array(['X','M','A','S'])
total = 0

for i, line in enumerate(lines):
    puzzle[i, :] = list(line.strip())

for r, row in enumerate(puzzle):
    for c, col in enumerate(row):
        view = puzzle[r:r+4,c:c+4]
        if np.array_equal(view[0], search_word):
            total += 1
        if np.array_equal(view[0], search_word[::-1]):
            total += 1
        if np.array_equal(view[0:,0], search_word):
            total += 1
        if np.array_equal(view[0:,0], search_word[::-1]):
            total += 1
        if np.array_equal(np.diagonal(view),search_word):
            total += 1
        if np.array_equal(np.diagonal(view),search_word[::-1]):
            total += 1
        if np.array_equal(np.fliplr(view).diagonal(),search_word):
            total += 1
        if np.array_equal(np.fliplr(view).diagonal(),search_word[::-1]):
            total += 1
print(total)

part2_total = 0
search_word = np.array(['M','A','S'])
for r, row in enumerate(puzzle):
    for c, col in enumerate(row):
        view = puzzle[r:r+3,c:c+3]
        if (np.array_equal(np.diagonal(view),search_word) or np.array_equal(np.diagonal(view),search_word[::-1])) and (np.array_equal(np.fliplr(view).diagonal(),search_word) or np.array_equal(np.fliplr(view).diagonal(),search_word[::-1])):
            part2_total += 1
print(part2_total)
