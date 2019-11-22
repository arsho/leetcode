"""
Title     : 704. Binary Search
Category  : Binary Search
URL       : https://leetcode.com/problems/binary-search/
Author    : arsho
Created   : 05 October 2019
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_length = len(nums)
        lower_index = 0
        higher_index = nums_length - 1
        while lower_index <= higher_index:
            mid = lower_index + (higher_index - lower_index) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lower_index = mid + 1
            else:
                higher_index = mid - 1
        return -1


if __name__ == "__main__":
    solution = Solution()
    input_ar = [-1, 0, 3, 5, 9, 12]
    input_target = 9
    expected_output = 4
    output = solution.search(input_ar, input_target)
    assert output == expected_output, input_ar

    solution = Solution()
    input_ar = [-1, 0, 3, 5, 9, 12]
    input_target = 2
    expected_output = -1
    output = solution.search(input_ar, input_target)
    assert output == expected_output, input_ar

    solution = Solution()
    input_ar = [5]
    input_target = 5
    expected_output = 0
    output = solution.search(input_ar, input_target)
    assert output == expected_output, input_ar

    solution = Solution()
    input_ar = [2, 3]
    input_target = 5
    expected_output = -1
    output = solution.search(input_ar, input_target)
    assert output == expected_output, input_ar

    solution = Solution()
    input_ar = [2, 3]
    input_target = 3
    expected_output = 1
    output = solution.search(input_ar, input_target)
    assert output == expected_output, input_ar
