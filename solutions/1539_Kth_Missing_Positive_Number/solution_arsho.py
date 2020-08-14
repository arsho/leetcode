"""
Title     : 1539. Kth Missing Positive Number
Category  : Hash Table
URL       : https://leetcode.com/problems/kth-missing-positive-number/
Author    : arsho
Created   : 14 August 2020
"""
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count_missing = 0
        current_number = 1
        d = {}
        for i in arr:
            d[i] = 0
        while count_missing < k:
            if current_number not in d:
                count_missing += 1
            if count_missing == k:
                break
            current_number += 1
        return current_number
