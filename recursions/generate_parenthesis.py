"""
https://leetcode.com/articles/generate-parentheses/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses
"""

class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                print (A)
                generate(A)
                A.pop()
                print (A)
                A.append(')')
                print (A)
                generate(A)
                print (A)
                A.pop()
                print (A)

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans

s = Solution()
ans = s.generateParenthesis(2)
print (ans)
