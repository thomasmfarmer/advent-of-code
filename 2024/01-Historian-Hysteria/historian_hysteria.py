#!/usr/bin/env python3
"""Module to process AOD 2024 Day One."""
import sys
from collections import Counter

data_filename = sys.argv[1]

with open(data_filename, 'r', encoding="utf-8") as file:
    one, two = [], []
    for line in file:
        a, b = line.strip().split()
        one.append(int(a))
        two.append(int(b))
    one.sort()
    two.sort()

    total_distance = sum(abs(a - b) for a, b in zip(one, two))

    c = Counter(one)
    similarity_score = sum(i * c.get(i, 0) for i in two)

    print(total_distance, similarity_score)
