# Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.

def is_palindrome(s):
    if s == s[::-1]:
        return 'Is palindrome'
    else:
        return 'not palindrome'


print(is_palindrome('abcba'))

print(is_palindrome('abcdw'))
