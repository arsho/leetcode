"""
Title     : 969. Pancake Sorting
Category  : Sort
URL       : https://leetcode.com/problems/pancake-sorting/
Author    : arsho
Created   : 25 August 2020
"""
from typing import List


class Solution:
    def get_max_element_index(self, A: List[int]) -> int:
        max_element_index = 0
        for i in range(len(A)):
            if A[i] >= A[max_element_index]:
                max_element_index = i
        return max_element_index

    def pancakeSort(self, A: List[int]) -> List[int]:
        current_size = len(A)
        res = []
        while current_size >= 1:
            max_element_index = self.get_max_element_index(A[:current_size])
            temp = A[:max_element_index + 1]
            A[:max_element_index + 1] = temp[::-1]
            temp = A[:current_size]
            A[:current_size] = temp[::-1]
            res.append(max_element_index + 1)
            res.append(current_size)
            current_size -= 1
        return res
