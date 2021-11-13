"""
Title     : 1346. Check If N and Its Double Exist
Category  : Array
URL       : https://leetcode.com/problems/check-if-n-and-its-double-exist/
Author    : arsho
Created   : 25 August 2020
"""
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        unique_nums = {}
        for i in arr:
            if i * 2 in unique_nums:
                return True
            if i % 2 == 0 and i // 2 in unique_nums:
                return True
            unique_nums[i] = 1
        return False
