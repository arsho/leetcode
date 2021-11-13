"""
Title     : 1021. Remove Outermost Parentheses
Category  : Stack
URL       : https://leetcode.com/problems/remove-outermost-parentheses/
Author    : arsho
Created   : 30 March 2021
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        output = ""
        b = 0
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(c)
            else:
                stack.pop(-1)
            if i != 0:
                if len(stack) == 0:
                    output += "".join(s[b + 1:i])
                    b = i + 1
        return output
