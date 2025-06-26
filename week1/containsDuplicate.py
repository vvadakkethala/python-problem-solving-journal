"""
Problem: Contains Duplicate
LeetCode Link: https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct..
"""

def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example usage
if __name__ == "__main__":
    nums = [1,1,1,3,3,4,3,2,4,2]
    result = containsDuplicate(nums)
    print("Contains Duplicate:", result)  # Output: False