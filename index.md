---
layout: default
title: Coding Challenges
---

# Table of Contents

- [Array](#array)
  - [Problem 1: Bubble Sort](#problem-1-bubble-sort)
  - [Problem 2: Merge Sort](#problem-2-merge-sort)
- [Linked List](#linked-list)
  - [Problem 1: Reverse Linked List](#problem-1-reverse-linked-list)
  - [Problem 2: Detect Cycle in Linked List](#problem-2-detect-cycle-in-linked-list)

# Array

## Problem 1: Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
