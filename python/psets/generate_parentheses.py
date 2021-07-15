from typing import List

"""
Generate all combinations of n ()

Each step we need to add ( and )
- `(` can be added n times
- `)` can be aded only if n_opnen > n_closed
- base case: if n_open and n_closed are n

             [(]
             /\
   [((]            [()]
    /\              /\
  #   [(()]     [()(] #
       /\        /\
      #  [(())] # [()()]
                
"""


def generate_parentheses(n: int) -> List[str]:
    ans = []
    parentheses = []

    def aux(n_open, n_closed):
        # base case, string finished
        if n_open == n and n_closed ==  n:
            ans.append(''.join(parentheses))
            return

        if n_open < n:
            parentheses.append('(')
            aux(n_open + 1, n_closed)
            parentheses.pop()

        if n_closed < n_open:
            parentheses.append(')')
            aux(n_open, n_closed + 1)
            parentheses.pop()

    aux(0, 0)
    return ans

if __name__ == "__main__":
    print(generate_parentheses(1))
    print(generate_parentheses(2))
    print(generate_parentheses(3))

