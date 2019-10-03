'''
Title     : 1207. Unique Number of Occurrences
Category  : Hash Table
URL       : https://leetcode.com/problems/unique-number-of-occurrences/
Author    : arsho
Created   : 03 October 2019
'''
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        return len(set(d.keys())) == len(set(d.values()))


if __name__ == "__main__":
    solution = Solution()
    arr = [1, 2, 2, 1, 1, 3]
    result = solution.uniqueOccurrences(arr)
    expected_result = True
    assert result == expected_result, arr

    arr = [1, 2]
    result = solution.uniqueOccurrences(arr)
    expected_result = False
    assert result == expected_result, arr

    arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    result = solution.uniqueOccurrences(arr)
    expected_result = True
    assert result == expected_result, arr
