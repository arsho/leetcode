'''
Title     : 1122. Relative Sort Array
Category  : Sort
URL       : https://leetcode.com/problems/relative-sort-array/
Author    : arsho
Created   : 04 October 2019
'''
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        for i in arr1:
            d[i] = d.get(i, 0) + 1
        result = []
        unlisted = []
        for i in arr2:
            temp = [i for j in range(d[i])]
            result += temp
        for i in d:
            if i not in arr2:
                temp = [i for j in range(d[i])]
                unlisted += temp
        unlisted = sorted(unlisted)
        return result + unlisted


if __name__ == "__main__":
    solution = Solution()
    input_ar_1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    input_ar_2 = [2, 1, 4, 3, 9, 6]
    output_ar = solution.relativeSortArray(input_ar_1, input_ar_2)
    expected_output_ar = [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    assert output_ar == expected_output_ar, input_ar_1
