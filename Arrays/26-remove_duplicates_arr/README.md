# 26. Remove Duplicates from Sorted Array

## Approach
Use two pointers:
- `i` stores the position of the next unique element.
- `j` traverses the array.
- When a new unique element is found, place it at index `i`.

## Time Complexity
O(n)

## Space Complexity
O(1)