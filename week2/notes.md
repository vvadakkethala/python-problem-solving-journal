## Day 1 - Valid Palindrome
In this problem, we are asked to determine if a given string is a palindrome, considering only alphanumeric characters and ignoring cases. A palindrome reads the same forward and backward.

To solve this, we can:
1. Filter out non-alphanumeric characters and convert the remaining characters to lowercase.
2. Use two pointers, one starting from the beginning and the other from the end, to compare characters.
3. If all corresponding characters match, the string is a palindrome; otherwise, it is not.


## Day 2 - Two Sum II - Input Array Is Sorted
In this problem, we are given a 1-indexed array of integers that is already sorted in non-decreasing order and a target number. We need to find two numbers such that they add up to the target and return their indices as an array [index1, index2].

To solve this, we can:
1. Use two pointers, one starting from the beginning and the other from the end of the array.
2. Calculate the sum of the numbers at the two pointers.
3. If the sum equals the target, return the indices (1-indexed).
4. If the sum is less than the target, move the left pointer to the right.
5. If the sum is greater than the target, move the right pointer to the left.
6. Repeat until the two pointers meet.

## Day 3 - 3Sum
In this problem, we are asked to find all unique triplets in an array that sum up to zero.

To solve this, we can:
1. Sort the array.
2. Iterate through the array with an index `i`.
3. For each `i`, use two pointers `left` and `right` to find pairs that sum up with `nums[i]` to zero.
4. Skip duplicate elements to avoid duplicate triplets.
5. If the sum of the triplet is zero, add it to the result list.
6. If the sum is less than zero, move the `left` pointer to the right.
7. If the sum is greater than zero, move the `right` pointer to the left.
8. Continue until all triplets are found.

## Day 4 - Remove Duplicates from Sorted Array II
In this problem, we are asked to remove duplicates from a sorted array such that each element appears at most twice and return the new length.

To solve this, we can:
1. If the array has 2 or fewer elements, return its length.
2. Use a pointer `j` starting at index 2 to track the position of the next unique element.
3. Iterate through the array starting from index 2 with a pointer `i`.
4. If `nums[i]` is not equal to `nums[j - 2]`, assign `nums[j] = nums[i]` and increment `j`.
5. Continue until the end of the array.
6. Return `j` as the new length of the array.

## Day 5 - Container With Most Water
In this problem, we are asked to find two lines in an array of non-negative integers that, together with the x-axis, form a container that holds the most water.

To solve this, we can:
1. Use two pointers, one starting from the beginning and the other from the end of the array.
2. Calculate the area formed by the lines at the two pointers and the x-axis.
3. Keep track of the maximum area found.
4. Move the pointer pointing to the shorter line inward, as moving the taller line won't increase the area.
5. Repeat until the two pointers meet.
6. Return the maximum area found.

