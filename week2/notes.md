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

