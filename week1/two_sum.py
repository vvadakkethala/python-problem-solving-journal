"""
Problem: Two Sum
LeetCode Link: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = twoSum(nums, target)
    print("Indices:", result)  # Output: [0, 1]