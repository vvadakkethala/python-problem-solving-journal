## Day 1 - Two Sum
In this problem, we are using a dictionary (hash map) called seen and we are adding the elements in nums list to this dictionary where key is the number and value is the index. A variable names complement is created which is the difference of target minus the number. if the complement is not there in the dictionary, then we add. if its there in the dictionary then we return the index of complement (i.e seen[complement]) and i

## Day 2 - Contains Duplicate
In this problem we need to return true if the element is repeated in the input nums list. so we create an empty set object and loop through nums, if the value num in nums is already present in the set return true else we add it for list once full loop is done and no elements repeated then we return false
