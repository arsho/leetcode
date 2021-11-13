"""
Title     : 1496. Path Crossing
Category  : String
URL       : https://leetcode.com/problems/path-crossing/
Author    : arsho
Created   : 29 June 2020
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        d = {}
        x = 0
        y = 0
        point = "{}{}".format(x, y)
        d[point] = 1
        for direction in path:
            if direction == "N":
                y += 1
            elif direction == "S":
                y -= 1
            elif direction == "E":
                x += 1
            elif direction == "W":
                x -= 1
            point = "{}{}".format(x, y)
            if point in d:
                return True
            d[point] = 1
        return False


if __name__ == "__main__":
    solution = Solution()

    test_case = "NESWW"
    expected_result = True
    result = solution.isPathCrossing(test_case)
    assert expected_result == result, "Error in '{}', Expected: {}, Got: {}".format(test_case, expected_result, result)

    test_case = "NES"
    expected_result = False
    result = solution.isPathCrossing(test_case)
    assert expected_result == result, "Error in {}, Expected: {}, Got: {}".format(test_case, expected_result, result)
