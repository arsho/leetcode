"""
Title     : 1323. Maximum 69 Number
Category  : Math
URL       : https://leetcode.com/problems/maximum-69-number/
Author    : arsho
Created   : 22 January 2020
"""
class Solution:
    def maximum69Number (self, num: int) -> int:
        ar = []
        while num > 0:
            ar.append(num%10)
            num = num // 10
        ar = ar[::-1]
        for i in range(len(ar)):
            if ar[i] == 6:
                ar[i] = 9
                break
        return int("".join([str(i) for i in ar]))