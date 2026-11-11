""" Problem: Two Sum II - Input Array Is Sorted : Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

You may assume that each input would have exactly one solution and you may not use the same element twice.

You must use only constant extra space. """


def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))  # [1, 2]
    print(twoSum([2,3,4], 6))      # [1, 3]
    print(twoSum([-1,0], -1))      # [1, 2]