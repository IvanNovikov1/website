def is_palindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


print(is_palindrome('шалаш'))
print(is_palindrome('дом'))
