"""
Title     : 27. Remove Element
Category  : Two Pointers
URL       : https://leetcode.com/problems/remove-element/
Author    : arsho
Created   : 23 August 2020
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total = len(nums)
        left = 0
        right = len(nums) - 1
        for i in range(right, -1, -1):
            if nums[i] != val:
                right = i
                break
        while left < right:
            if nums[left] == val:
                total -= 1
                nums[left], nums[right] = nums[right], nums[left]
                for i in range(right, -1, -1):
                    if nums[i] != val:
                        right = i
                        break
            left += 1
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                return i
            count += 1
        if count == len(nums):
            return count
        return 0
