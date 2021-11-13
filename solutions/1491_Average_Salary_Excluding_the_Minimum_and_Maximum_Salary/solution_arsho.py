"""
Title     : 1491. Average Salary Excluding the Minimum and Maximum Salary
Category  : Sort
URL       : https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
Author    : arsho
Created   : 29 June 2020
"""
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
