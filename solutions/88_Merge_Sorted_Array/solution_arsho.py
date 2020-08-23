"""
Title     : 88. Merge Sorted Array
Category  : Two Pointers
URL       : https://leetcode.com/problems/merge-sorted-array/
Author    : arsho
Created   : 23 August 2020
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        max_position = m + n - 1
        pos = max_position
        first_pointer = m - 1
        second_pointer = n - 1
        for i in range(max_position, -1, -1):
            if first_pointer >= 0 and second_pointer >= 0:
                if nums1[first_pointer] > nums2[second_pointer]:
                    nums1[i] = nums1[first_pointer]
                    first_pointer -= 1
                else:
                    nums1[i] = nums2[second_pointer]
                    second_pointer -= 1
            elif first_pointer < 0:
                nums1[i] = nums2[second_pointer]
                second_pointer -= 1
            elif second_pointer < 0:
                nums1[i] = nums1[first_pointer]
                first_pointer -= 1
