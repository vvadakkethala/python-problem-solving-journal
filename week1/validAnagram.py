"""
Problem: Valid Anagram
LeetCode Link: https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    for char in t:
        if char not in freq or freq[char]==0:
            return False
        freq[char]-=1
    return True

# Example usage
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    result = isAnagram(s, t)
    print("Is Anagram:", result)  # Output: True
    s = "rat"
    t = "car"
    result = isAnagram(s, t)
    print("Is Anagram:", result)  # Output: False