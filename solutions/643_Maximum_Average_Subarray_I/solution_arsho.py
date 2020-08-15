"""
Title     : 643. Maximum Average Subarray I
Category  : Array
URL       : https://leetcode.com/problems/maximum-average-subarray-i/
Author    : arsho
Created   : 15 August 2020
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[0:k])
        max_average = current_sum / k
        for i in range(1, len(nums) - k + 1):
            current_sum -= nums[i - 1]
            current_sum += nums[i + k - 1]
            max_average = max(max_average, current_sum / k)
        return max_average
