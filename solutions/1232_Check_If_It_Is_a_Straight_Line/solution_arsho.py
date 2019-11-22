"""
Title     : 1232. Check If It Is a Straight Line
Category  : Math
URL       : https://leetcode.com/problems/check-if-it-is-a-straight-line/
Author    : arsho
Created   : 22 November 2019
"""
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        m_prev = None
        for i in range(1, len(coordinates)):
            rise = coordinates[i][1] - coordinates[i - 1][1]
            run = coordinates[i][0] - coordinates[i - 1][0]
            if run == 0:
                return False
            m = rise / run
            if not m_prev:
                m_prev = m
            else:
                if m != m_prev:
                    return False
                m_prev = m
        return True


if __name__ == "__main__":
    solution = Solution()

    coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    output = solution.checkStraightLine(coordinates)
    expected_output = True
    assert output == expected_output, coordinates

    coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
    output = solution.checkStraightLine(coordinates)
    expected_output = False
    assert output == expected_output, coordinates

    coordinates = [[-1, 1], [-6, -4], [-6, 2], [2, 0], [-1, -2], [0, -4]]
    output = solution.checkStraightLine(coordinates)
    expected_output = False
    assert output == expected_output, coordinates
