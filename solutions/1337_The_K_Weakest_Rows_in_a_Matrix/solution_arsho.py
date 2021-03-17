"""
Title     : 1337. The K Weakest Rows in a Matrix
Category  : Array
URL       : https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
Author    : arsho
Created   : 17 March 2021
"""
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        data = []
        for i, row in enumerate(mat):
            data.append([i, sum(row)])
        data = sorted(data, key=lambda x: (x[1], x[0]))
        return [i[0] for i in data][:k]
