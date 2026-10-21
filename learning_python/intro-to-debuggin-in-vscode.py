def encrypt_message(word):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    new_word = ""
    for letter in word:
        if letter in alphabets:
            print(f"letter is {letter}")
            new_letter = alphabets[(alphabets.index(letter)+2) % 26]
            print(f"new letter is {new_letter}")
            new_word+=new_letter
    return new_word

print(encrypt_message("zab"))