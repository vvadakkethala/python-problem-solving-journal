""" Problem: Majority Element. Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.."""


def majorityElement(nums: list[int]) -> int:
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > len(nums) // 2:
            return num
        

# Example usage
if __name__ == "__main__":
    nums = [3, 2, 3]
    print(majorityElement(nums))  # Output: 3

    nums = [2, 2, 1, 1, 1, 2, 2]
    print(majorityElement(nums))  # Output: 2