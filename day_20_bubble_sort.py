#!/bin/python3

import sys

n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
counter_swaps = 0

for i in range(n):
    current_swaps = 0

    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            current_swaps += 1
            counter_swaps += 1

    if current_swaps == 0:
        break

print(f"Array is sorted in {counter_swaps} swaps.")
print(f"First Element: {arr[0]}")
print(f"Last Element: {arr[-1]}")
