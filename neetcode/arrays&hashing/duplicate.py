''' 
CONTAINS DUPLICATE
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1: [1,2,3,1] => True

Example 2: [1,2,3,4] => False
'''

def containsDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
    
# Time complexity: O(n)
# Space complexity: O(n)

print(containsDuplicate([1,2,3,3,4,5])) # True