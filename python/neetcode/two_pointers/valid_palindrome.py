# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
# removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

from operator import is_


def is_palindrome(s: str) -> bool:
    def is_alpha(c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z')) \
            or (ord('a') <= ord(c) <= ord('z')) \
            or (ord('0') <= ord(c) <= ord('9'))

    lp = 0
    rp = len(s) - 1
    
    while lp < rp:
        while lp < rp and not is_alpha(s[lp]):
            lp += 1
        
        while lp < rp and not is_alpha(s[rp]):
            rp -= 1
        
        if s[lp].lower() != s[rp].lower():
            return False

        lp += 1
        rp -= 1
    return True
            
if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert is_palindrome("race a car") is False