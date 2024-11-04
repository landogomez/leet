''' 
Two Sum Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example 1: nums = [2,7,11,15], target = 9 => [0,1]

'''

def twoSum(nums, target):
    prevMap = {} # val -> index

    for i, n in enumerate(nums): #enumerate itera sobre un iterable y devuelve el índice y el valor de los elementos del iterable.
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

print(twoSum([5,5], 10)) # [0,1]

