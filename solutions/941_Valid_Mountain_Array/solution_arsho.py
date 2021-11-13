'''
Title     : 941. Valid Mountain Array
Category  : Array
URL       : https://leetcode.com/problems/valid-mountain-array/
Author    : arsho
Created   : 07 June 2019
'''
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        a_length = len(A)
        if a_length < 3:
            return False
        prev_value = None
        decreasing_sequence_found = False
        increasing_sequence_found = False
        for i, val in enumerate(A):
            if prev_value == None:
                prev_value = val
            else:
                if val == prev_value:
                    return False
                elif val > prev_value:
                    if decreasing_sequence_found:
                        return False
                    increasing_sequence_found = True
                elif val < prev_value:
                    decreasing_sequence_found = True
                prev_value = val
        return increasing_sequence_found and decreasing_sequence_found


if __name__ == '__main__':
    solution = Solution()

    ar = [2, 1]
    result = solution.validMountainArray(ar)
    expected_result = False
    assert result == expected_result, (ar, result, expected_result)

    ar = [3, 5, 5]
    result = solution.validMountainArray(ar)
    expected_result = False
    assert result == expected_result, (ar, result, expected_result)

    ar = [0, 3, 2, 1]
    result = solution.validMountainArray(ar)
    expected_result = True
    assert result == expected_result, (ar, result, expected_result)

    ar = [2, 0, 2]
    result = solution.validMountainArray(ar)
    expected_result = False
    assert result == expected_result, (ar, result, expected_result)

    ar = [0, 1, 2, 4, 2, 1]
    result = solution.validMountainArray(ar)
    expected_result = True
    assert result == expected_result, (ar, result, expected_result)

    ar = [3, 7, 6, 4, 3, 0, 1, 0]
    result = solution.validMountainArray(ar)
    expected_result = False
    assert result == expected_result, (ar, result, expected_result)

    ar = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    result = solution.validMountainArray(ar)
    expected_result = False
    assert result == expected_result, (ar, result, expected_result)

    ar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = solution.validMountainArray(ar)
    expected_result = False
    assert result == expected_result, (ar, result, expected_result)
