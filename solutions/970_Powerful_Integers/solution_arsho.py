'''
Title     : 970. Powerful Integers
Category  : Math
URL       : https://leetcode.com/problems/powerful-integers/
Author    : arsho
Created   : 06 January 2019
'''


class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        d = {}
        for i in range(101):
            for j in range(101):
                n = x ** i + y ** j
                if n <= bound:
                    d[n] = 1
        ar = list(d.keys())
        return ar


if __name__ == '__main__':
    x1 = 2
    y1 = 3
    bound1 = 10
    s1 = Solution().powerfulIntegers(x1, y1, bound1)
    e1 = [2, 3, 4, 5, 7, 9, 10]
    # assert s1 == e1

    x1 = 3
    y1 = 5
    bound1 = 15
    s1 = Solution().powerfulIntegers(x1, y1, bound1)
    e1 = [2, 4, 6, 8, 10, 14]
    # assert s1 == e1

    x1 = 90
    y1 = 90
    bound1 = 10 ** 6
    s1 = Solution().powerfulIntegers(x1, y1, bound1)
