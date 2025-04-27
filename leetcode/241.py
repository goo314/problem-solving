"""LeetCode

Algorithm : 
    DFS
Level :
    Medium
Status :
    Failed

Fri Sep 20 00:17:28 KST 2024
"""

from itertools import *

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        """
        result = []
        nums, ops = [], []

        for i in range(len(expression)-1):
            if expression[i] in ['+', '-', '*']:
                ops.append(expression[i])
            elif expression[i+1] in ['+', '-', '*']:
                nums.append(int(expression[i]))
            else:
                nums.append(int(expression[i]+expression[i+1]))

        n = len(ops)
        index = [i for i in range(n)]
        cases = permutations(index, n)
        
        for case in cases:
            val = 0
            for i in case:
                if ops[i] == '+':
                    val
            result.append(val)
        """

        def compute(expr):
            ans = []
            
            n = len(expr)
            for i in range(n):
                op = expr[i]
                if op in ["+", "-", "*"]:
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])

                    for l in left:
                        for r in right:
                            if op == "+":
                                ans.append(l+r)
                            elif op == "-":
                                ans.append(l-r)
                            else:
                                ans.append(l*r)
            if not ans:
                ans.append(int(expr))
            return ans

        return compute(expression)
                    
        