""" Problem: Intersection of Two Arrays II  Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order. """

from collections import Counter

def intersect(nums1, nums2):
    counts = Counter(nums1)
    intersection = []
    for num in nums2:
        if counts[num] > 0:
            intersection.append(num)
            counts[num] -= 1
    return intersection

# Example usage
if __name__ == "__main__":
    nums1 = [4,9,5]
    nums2 = [9, 4, 9, 8, 4]
    print(intersect(nums1, nums2))