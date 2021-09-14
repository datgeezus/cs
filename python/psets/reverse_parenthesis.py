# You are given a string s that consists of lower case English letters and brackets. 

# Reverse the strings in each pair of matching parentheses, starting from the innermost one.

# Your result should not contain any brackets.

from collections import deque

def reverse_parentheses(s: str) -> str:
    q = deque()
    for char in s:
        q.append(char)
        if q[-1] == ")":
            q.pop()  # remove "("
            word = []
            while q and q[-1] != "(":
                word.append(q.pop())
            if q: q.pop()  # remove "("
            for w in word:
                q.append(w)
    
    return "".join(q)

if __name__ == "__main__":
    print(reverse_parentheses("(abcd)"))  # dcba
    print(reverse_parentheses("(u(love)i)"))  # iloveu
    print(reverse_parentheses("(ed(et(oc))el)"))  # leetcode
    print(reverse_parentheses("a(bcdefghijkl(mno)p)q"))  # apmnolkjihgfedcbq