#!/usr/bin/env python3
"""Module to process AOD 2024 day two."""
import sys
from itertools import pairwise
from typing import Iterable

def is_strictly_increasing(report: list[int]) -> bool:
    return all(l < r and 1 <= r - l <= 3 for l, r in pairwise(report))

def is_safe(report: list[int]) -> bool:
    return is_strictly_increasing(report) or is_strictly_increasing(report[::-1])

def omit_one(report: list[int]) -> Iterable[list[int]]:
    for index in range(len(report)):
        yield report[:index] + report[index + 1 :]

data_filename = sys.argv[1]

reports = [list(map(int, line.strip().split()))
            for line in open(data_filename, 'r', encoding="utf-8")]

print(sum(map(is_safe, reports)))
print(sum(is_safe(l) or any(is_safe(o) for o in omit_one(l)) for l in reports))
