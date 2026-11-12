""" Problem: Remove Duplicates from Sorted Array II.

Given a sorted array nums, remove the duplicates in-place such that each element appears at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory. """


def removeDuplicates(nums: list[int]) -> int:
    if len(nums) <= 2:
        return len(nums)
    
    j = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[j - 2]:
            nums[j] = nums[i]
            j += 1
    return j

# Example usage
if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    length = removeDuplicates(nums)
    print(length)  # Output: 5
    print(nums[:length])  # Output: [1, 1, 2, 2, 3]
