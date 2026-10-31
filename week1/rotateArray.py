""" Problem: Rotate Array.

Given an array, rotate the array to the right by k steps, where k is non-negative.
"""

# def rotate(nums: list[int], k: int) -> None:
#     n = len(nums)
#     k %= n
#     nums[:] = nums[-k:] + nums[:-k]


def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n
    def reverse(start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    
    
    

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)
    print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
