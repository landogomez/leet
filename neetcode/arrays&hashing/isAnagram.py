'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An anagram is a word formed by rearranging the letters of another, such as cinema, formed from iceman.

Example 1: s = "anagram", t = "nagaram" => True
Example 2: s = "rat", t = "car" => False

'''

def isAnagram(s ,t):
    if len(s) != len(t):
        return False
    
    sorted_s = sorted(s)
    sorted_t = sorted(t)

    if sorted_s == sorted_t:
        return True
    return False

print(isAnagram("car", "")) # True