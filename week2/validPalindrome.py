""" Problem: Valid Palindrome : A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise. """


def validPalindrome(s: str) -> bool:
    
    filtered_chars = [c.lower() for c in s if c.isalnum()]
    
    left, right = 0, len(filtered_chars) - 1
    while left < right:
        if filtered_chars[left] != filtered_chars[right]:
            return False
        left += 1
        right -= 1
    return True

# Example usage
if __name__ == "__main__":
    print(validPalindrome("A man, a plan, a canal: Panama"))  # True
    print(validPalindrome("race a car"))                      # False
    print(validPalindrome(" "))                               # True
    print(validPalindrome("0P"))                              # False