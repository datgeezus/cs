"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]

 

Constraints:

    0 <= rowIndex <= 33

 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""

def memo(fn):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        cache[args] = fn(*args)
        return cache[args]
    return wrapper

def get_row(row_index: int) -> list[int]:

    @memo
    def get_num(r: int, c: int) -> int:
        if r == 0 or c == 0 or r == c:
            return 1
        return  get_num(r - 1, c - 1) + get_num(r - 1, c)

    ans = []
    for i in range(row_index + 1):
        ans.append(get_num(row_index, i))

    return ans



if __name__ == "__main__":
    ans = get_row(3)
    print(ans)

    ans = get_row(300)
    print(ans)
