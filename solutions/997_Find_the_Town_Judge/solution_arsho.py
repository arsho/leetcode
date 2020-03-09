"""
Title     : 997. Find the Town Judge
Category  : Graph
URL       : https://leetcode.com/problems/find-the-town-judge/
Author    : arsho
Created   : 09 March 2020
"""
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        d = {}
        for pair in trust:
            people, judge = pair
            d[people] = 0
            if judge not in d:
                d[judge] = 1
            elif judge in d and d[judge] != 0:
                d[judge] += 1

        potential_judges = [key for key in d.keys() if d[key] == N - 1]
        if len(potential_judges) != 1:
            return -1
        return potential_judges[0]
