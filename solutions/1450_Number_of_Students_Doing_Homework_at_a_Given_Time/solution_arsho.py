"""
Title     : 1450. Number of Students Doing Homework at a Given Time
Category  : Array
URL       : https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
Author    : arsho
Created   : 20 May 2020
"""


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int],
                    queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        return count
