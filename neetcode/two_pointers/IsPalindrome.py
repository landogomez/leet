'''
Is Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

A palindrome is a word that reads the same backward as forward.

Example 1: Input: s = "Was it a car or a cat I saw?" => True


'''

def isPalindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]