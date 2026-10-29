""" Problem: Reverse String. Reverse the input string. """


def reverseString(s: str) -> None:
    i = 0
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
        
## Example usage
if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    reverseString(s)
    print(s)  # Output: ['o', 'l', 'l', 'e', 'h']
    s = ["H", "e", "l", "l", "o"]
    reverseString(s)
    print(s)  # Output: ['o', 'l', 'l', 'e', 'H']
    s = ["a"]
    reverseString(s)
    print(s)  # Output: ['a']
    s = []
    reverseString(s)
    print(s)  # Output: []