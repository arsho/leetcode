"""
Title     : 1299. Replace Elements with Greatest Element on Right Side
Category  : Array
URL       : https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
Author    : arsho
Created   : 26 August 2020
"""
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value_index = 0
        max_value = -1
        for i in range(len(arr)):
            if max_value_index == i:
                max_value = -1
                for j in range(i + 1, len(arr)):
                    if arr[j] > max_value:
                        max_value = arr[j]
                        max_value_index = j
            arr[i] = max_value
        return arr
