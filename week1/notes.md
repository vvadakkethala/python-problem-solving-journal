## Day 1 - Two Sum
In this problem, we are using a dictionary (hash map) called seen and we are adding the elements in nums list to this dictionary where key is the number and value is the index. A variable names complement is created which is the difference of target minus the number. if the complement is not there in the dictionary, then we add. if its there in the dictionary then we return the index of complement (i.e seen[complement]) and i

## Day 2 - Contains Duplicate
In this problem we need to return true if the element is repeated in the input nums list. so we create an empty set object and loop through nums, if the value num in nums is already present in the set return true else we add it for list once full loop is done and no elements repeated then we return false

## Day 3 - Valid Anagram
In this problem we create a dictionary (hashmap) where key is each character and value is its frequency. then we check the other strings character if the character of the other string is not there in the frequency hashmap, then we return false, if its there then we reduce the value -=1. once all loop is complete and did not break in between, then we return true. 

## Day 4 - Maximum Subarray
In this problem, we parse through each element in the array. we keep a track of 2 variables curren_sum and max_sum. we take max out of these 2 values. we initialize current sum and max sum with the number at the first index then we add next element to the current sum. if that is max then store in the max_sum else we keep the current value which is in the max_sum. finally we return max_sum