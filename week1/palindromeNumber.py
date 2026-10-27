""" Problem: Palindrome Number. Determine whether an integer is a palindrome. """


def isPalindrome(x: int) -> bool:
    """
    Determine whether an integer is a palindrome.
    """
    
    if x == 0:
        return True
    if x < 0 or x % 10 == 0:
        return False

    reversed_num = 0
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10

    return x == reversed_num or x == reversed_num // 10

# Example usage
if __name__ == "__main__":
    print(isPalindrome(121))  # True
    print(isPalindrome(-121)) # False
    print(isPalindrome(10))   # False
    print(isPalindrome(0))    # True
    print(isPalindrome(12321)) # True
    print(isPalindrome(123))   # False