'''
Title     : 1051. Height Checker
Category  : Array
URL       : https://leetcode.com/problems/height-checker/
Author    : arsho
Created   : 07 June 2019
'''
class Solution:
    def heightChecker(self, heights) -> int:
        sorted_height = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sorted_height[i]:
                count += 1
        return count

if __name__ == '__main__':
    solution = Solution()
    ar = [1,1,4,2,1,3]
    result = solution.heightChecker(ar)
    expected_result = 3
    assert result == expected_result, (ar, result, expected_result)

    ar = [1,2,1,2,1,1,1,2,1]
    result = solution.heightChecker(ar)
    expected_result = 4
    assert result == expected_result, (ar, result, expected_result)
