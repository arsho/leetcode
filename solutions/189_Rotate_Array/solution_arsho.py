"""
Title     : 189. Rotate Array
Category  : Array
URL       : https://leetcode.com/problems/rotate-array/
Author    : arsho
Created   : 09 March 2020
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums)
        temp = [0 for _ in range(nums_length)]
        for i in range(nums_length):
            new_pos = (i + k) % nums_length
            temp[new_pos] = nums[i]
        for i in range(nums_length):
            nums[i] = temp[i]
