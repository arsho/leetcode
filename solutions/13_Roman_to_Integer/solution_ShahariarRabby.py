"""
Title     : 13. Roman to Integer
Category  : Easy
URL       : https://leetcode.com/problems/roman-to-integer/
Author    : ShahariarRabby
Created   : 13 November 2021
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000, }
        IV = s.count('IV')
        s = s.replace('IV', '')
        IV = IV * 4

        IX = s.count('IX')
        s = s.replace('IX', '')
        IX = IX * 9

        XL = s.count('XL')
        s = s.replace('XL', '')
        XL = XL * 40

        XC = s.count('XC')
        s = s.replace('XC', '')
        XC = XC * 90

        CD = s.count('CD')
        s = s.replace('CD', '')
        CD = CD * 400

        CM = s.count('CM')
        s = s.replace('CM', '')
        CM = CM * 900

        sum_num = IV + IX + XL + XC + CD + CM

        for i in range(len(s)):
            cur_val = values.get(s[i])
            sum_num += cur_val
        return sum_num