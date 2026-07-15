class Solution(object):
    def removeDuplicates(self, nums):
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1

        return i
    """
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
    """