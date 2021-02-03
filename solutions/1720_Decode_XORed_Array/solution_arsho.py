"""
Title     : 1720. Decode XORed Array
Category  : Bit Manipulation
URL       : https://leetcode.com/problems/decode-xored-array/
Author    : arsho
Created   : 03 February 2021
"""
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        original_ar = [first]
        for i in encoded:
            original_ar.append(original_ar[-1] ^ i)
        return original_ar
