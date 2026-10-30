""" Problem: Remove Element. Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k."""


def removeElement(nums: list[int], val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

## Example usage
if __name__ == "__main__":
    nums = [1, 1, 2]
    length = removeElement(nums, 1)
    print(length)  # Output: 2
    print(nums[:length])  # Output: [1, 2]

    nums = [0,0,1,1,1,2,2,3,3,4]
    length = removeElement(nums, 1)
    print(length)  # Output: 8
    print(nums[:length])  # Output: [0, 0, 2, 2, 3, 3, 4]