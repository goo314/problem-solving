"""Practices

Algorithm :
    Stack
Level :
    Easy
"""
class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', '}': '{', ']': '['}
        st = []
        for x in s:
            if x in ['(', '{', '[']:
                st.append(x)
            elif len(st)>0 and st[-1] == d[x]:
                st.pop()
            else:
                return False
        return len(st) == 0
