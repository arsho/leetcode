"""
Title     : 1281. Subtract the Product and Sum of Digits of an Integer
Category  : Math
URL       : https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
Author    : arsho
Created   : 09 December 2019
"""
from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = list(str(n))
        return reduce(lambda a, b: int(a)*int(b), s, 1) - \
               reduce(lambda a, b: int(a)+int(b), s, 0)


if __name__ == "__main__":
    solution = Solution()

    n = 234
    expected_output = 15
    assert solution.subtractProductAndSum(n) == expected_output, n

    n = 4421
    expected_output = 21
    assert solution.subtractProductAndSum(n) == expected_output, n
