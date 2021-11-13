"""
Title     : 1736. Latest Time by Replacing Hidden Digits
Category  : Greedy
URL       : https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/
Author    : arsho
Created   : 01 February 2021
"""


class Solution:
    def maximumTime(self, time: str) -> str:
        time_content = list(time)
        max_limit = list("23:59")
        if time_content[0] == "?":
            if time_content[1] != "?" and int(time_content[1]) > 3:
                max_limit[0] = "1"
        elif time_content[0] != "2":
            max_limit[1] = "9"
        for i, c in enumerate(time_content):
            if c == "?":
                time_content[i] = max_limit[i]
        return "".join(time_content)
