"""
Problem: Maximum Subarray
LeetCode Link: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""

def maxSubArray(nums: list[int]) -> int:
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
# Example usage
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = maxSubArray(nums)
    print("Maximum Subarray Sum:", result)  # Output: 6