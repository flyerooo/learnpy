def isPalindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[len(s) - 1]:
        return False
    else:
        return isPalindrome(s[1: len(s) - 1])

def main():
    print("Is moon a palindrome?", isPalindrome("moon"))

main()