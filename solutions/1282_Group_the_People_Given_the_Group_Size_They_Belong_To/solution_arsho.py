"""
Title     : 1282. Group the People Given the Group Size They Belong To
Category  : Greedy
URL       : https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
Author    : arsho
Created   : 29 June 2020
"""
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        result = []
        for i, size in enumerate(groupSizes):
            if size not in d:
                d[size] = [i]
            else:
                d[size].append(i)
            if len(d[size]) == size:
                result.append(d[size])
                del d[size]
        return result
