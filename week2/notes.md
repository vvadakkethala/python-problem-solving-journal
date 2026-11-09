## Day 1 - Valid Palindrome
In this problem, we are asked to determine if a given string is a palindrome, considering only alphanumeric characters and ignoring cases. A palindrome reads the same forward and backward.

To solve this, we can:
1. Filter out non-alphanumeric characters and convert the remaining characters to lowercase.
2. Use two pointers, one starting from the beginning and the other from the end, to compare characters.
3. If all corresponding characters match, the string is a palindrome; otherwise, it is not.