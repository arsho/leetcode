'''
Title     : 1200. Minimum Absolute Difference
Category  : Array
URL       : https://leetcode.com/problems/minimum-absolute-difference/
Author    : arsho
Created   : 01 October 2019
'''
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        result = []
        arr = sorted(arr)
        arr_length = len(arr)
        min_diff = 10**9
        for i in range(1, arr_length):
            min_diff = min(min_diff, abs(arr[i] - arr[i-1]))
        for i in range(arr_length):
            for j in range(i+1, arr_length):
                if abs(arr[i] - arr[j]) == min_diff:
                    result.append([arr[i], arr[j]])
                if abs(arr[i] - arr[j]) > min_diff:
                    break
        return result


if __name__ == "__main__":
    solution = Solution()
    arr = [4, 2, 1, 3]
    output = solution.minimumAbsDifference(arr)
    expected_output = [[1, 2], [2, 3], [3, 4]]
    assert output == expected_output, output

    arr = [1, 3, 6, 10, 15]
    output = solution.minimumAbsDifference(arr)
    expected_output = [[1, 3]]
    assert output == expected_output, output

    arr = [3, 8, -10, 23, 19, -4, -14, 27]
    output = solution.minimumAbsDifference(arr)
    expected_output = [[-14, -10], [19, 23], [23, 27]]
    assert output == expected_output, output
