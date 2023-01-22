"""
Title     : 2545. Sort the Students by Their Kth Score
Category  : Sort
URL       : https://leetcode.com/problems/sort-the-students-by-their-kth-score/
Author    : arsho
Created   : 22 January 2023
"""
from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> \
            List[List[int]]:
        return sorted(score, key=lambda x: x[k], reverse=True)
