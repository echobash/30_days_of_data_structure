
markdown
Copy
Edit
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
Problem 2: Merge Sort
python
Copy
Edit
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr
Linked List
Problem 1: Reverse Linked List
python
Copy
Edit
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

Problem 2: Detect Cycle in Linked List

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
