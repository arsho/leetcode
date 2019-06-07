'''
Title     : 941. Valid Mountain Array
Category  : Array
URL       : https://leetcode.com/problems/valid-mountain-array/
Author    : arsho
Created   : 07 June 2019
'''


class Solution:
    def validMountainArray(self, A) -> bool:
        ar_len = len(A)
        if ar_len < 3:
            return False
        found_increasing = False
        found_decreasing = True
        position = 0
        for i in range(0, ar_len - 1):
            if A[i + 1] > A[i]:
                found_increasing = True
                position = i + 1
            else:
                break

        if position == ar_len-1:
            found_decreasing = False

        for i in range(position, ar_len - 1):
            if A[i + 1] >= A[i]:
                found_decreasing = False
                break
        return found_increasing and found_decreasing


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
