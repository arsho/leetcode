"""
Title     : 342. Power of Four
Category  : Bit Manipulation
URL       : https://leetcode.com/problems/power-of-four/
Author    : arsho
Created   : 05 August 2020
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        """ Returns if a given number is a power of four.

        Arguments:
        num -- number to check (type: int)

        Each power of four has even number of zeros in binary representation
           4 =             100
          16 =           10000
          64 =         1000000
         256 =       100000000
        """

        s = bin(num)[2:]
        count_zeros = s[1:].count("0")
        return s[0] == "1" and count_zeros == len(
            s) - 1 and count_zeros % 2 == 0
