""" Problem: Move Zeroes. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array."""


def moveZeroes(nums):
    """
    Move all zeroes in the list to the end while maintaining the order of non-zero elements.
    """
    last_non_zero_found_at = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
            last_non_zero_found_at += 1
            

# Example usage
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    print(nums)  # Output: [1, 3, 12, 0, 0]
