"""
Title     : 53. Maximum Subarray
Category  : Dynamic Programming
URL       : https://leetcode.com/problems/maximum-subarray/
Author    : arsho
Created   : 09 April 2020
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum


if __name__ == "__main__":
    solution = Solution()
    input_ar = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected_output = 6
    output = solution.maxSubArray(input_ar)
    assert output == expected_output, (input_ar, output, expected_output)

    input_ar = [-2147483647]
    expected_output = -2147483647
    output = solution.maxSubArray(input_ar)
    assert output == expected_output, (input_ar, output, expected_output)

    input_ar = [-2, -1]
    expected_output = -1
    output = solution.maxSubArray(input_ar)
    assert output == expected_output, (input_ar, output, expected_output)

    input_ar = [-2, -3, -1]
    expected_output = -1
    output = solution.maxSubArray(input_ar)
    assert output == expected_output, (input_ar, output, expected_output)
