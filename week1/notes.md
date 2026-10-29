## Day 1 - Two Sum
In this problem, we are using a dictionary (hash map) called seen and we are adding the elements in nums list to this dictionary where key is the number and value is the index. A variable names complement is created which is the difference of target minus the number. if the complement is not there in the dictionary, then we add. if its there in the dictionary then we return the index of complement (i.e seen[complement]) and i

## Day 2 - Contains Duplicate
In this problem we need to return true if the element is repeated in the input nums list. so we create an empty set object and loop through nums, if the value num in nums is already present in the set return true else we add it for list once full loop is done and no elements repeated then we return false

## Day 3 - Valid Anagram
In this problem we create a dictionary (hashmap) where key is each character and value is its frequency. then we check the other strings character if the character of the other string is not there in the frequency hashmap, then we return false, if its there then we reduce the value -=1. once all loop is complete and did not break in between, then we return true. 

## Day 4 - Maximum Subarray
In this problem, we parse through each element in the array. we keep a track of 2 variables curren_sum and max_sum. we take max out of these 2 values. we initialize current sum and max sum with the number at the first index then we add next element to the current sum. if that is max then store in the max_sum else we keep the current value which is in the max_sum. finally we return max_sum.

Kadane’s algorithm helps you find the biggest total you can make by adding numbers that sit next to each other in a list. Imagine walking along the list and carrying a running score: at each number, you choose whether to add it to your score or drop the old score and start fresh with this number. You also keep a note of the highest score you’ve had so far, so a later smaller score won’t make you forget the best one. For example, in [-2, 1, -3, 4, -1, 2, 1], it finds [4, -1, 2, 1], which adds up to 6.

## Day 5 - Best Time to Buy and Sell Stock
In this problem we initiate 2 variables and set them to values as follows, min_price = flot('inf') and max_profit = 0. then we go through price of each day. if the current price is less than min_price, then we update min_price to that price, else we set max_profit to max(max_profit, price-min_price). finally we return the profit

## Day 6 - Merge Sorted Array
In this problem, we are given two sorted arrays, nums1 and nums2, where nums1 has enough space to hold all elements of both arrays. We use three pointers: i for the last element in the initial part of nums1, j for the last element in nums2, and k for the last position in nums1. We compare elements from the end and place the larger one at position k, then move the pointers accordingly. Finally, if any elements are left in nums2, we copy them to nums1.


## Day 7 - Intersection of Two Arrays II
In this problem, we use a Counter (hash map) to count the frequency of each element in the first array, nums1. Then, we iterate through the second array, nums2, and check if the element exists in the Counter with a positive count. If it does, we add it to the intersection list and decrement the count in the Counter. Finally, we return the intersection list containing elements that appear in both arrays as many times as they appear in both.

## Day 8 - Plus One
In this problem, we are given a list of digits representing a large integer. We need to increment this integer by one and return the resulting list of digits. We start from the last digit and move towards the first. If the current digit is less than 9, we simply increment it and return the list. If the digit is 9, we set it to 0 and continue to the next digit. If all digits are 9, we add a new digit 1 at the beginning of the list.

## Day 9 - Move Zeroes
In this problem, we need to move all zeroes in the list to the end while maintaining the order of non-zero elements. We use a pointer last_non_zero_found_at to keep track of the position of the last non-zero element. We iterate through the list, and whenever we find a non-zero element, we swap it with the element at last_non_zero_found_at and increment the pointer. This ensures that all non-zero elements are moved to the front, and zeroes are pushed to the end.

## Day 10 - Palindrome Check
In this problem, we need to determine whether a given integer is a palindrome. A palindrome is a number that reads the same backward as forward. We first handle edge cases: if the number is negative or ends with a zero (but is not zero itself), it cannot be a palindrome. We then reverse the second half of the number and compare it with the first half. If they are equal, the number is a palindrome; otherwise, it is not.

## Day 11 - Reverse String
In this problem, we need to reverse the input string in-place. We use two pointers, one starting at the beginning of the string and the other at the end. We swap the characters at these pointers and move the pointers towards each other until they meet in the middle. This effectively reverses the string without using extra space.

## Day 12 - Remove Duplicates from Sorted Array
In this problem, we need to remove duplicates from a sorted array in-place and return the new length of the array. We use a pointer i to keep track of the position of the last unique element. We iterate through the array with another pointer j, and whenever we find an element that is different from nums[i], we increment i and update nums[i] with nums[j]. Finally, we return i + 1 as the new length of the array containing only unique elements.