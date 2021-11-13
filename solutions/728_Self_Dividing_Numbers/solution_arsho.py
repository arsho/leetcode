'''
Title     : 728. Self Dividing Numbers
Category  : Math
URL       : https://leetcode.com/problems/self-dividing-numbers/
Author    : arsho
Created   : 14 January 2019
'''


class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ar = []
        for i in range(left, right + 1):
            cur = i
            flag = True
            s = str(cur)
            for c in s:
                if c == '0' or cur % int(c) != 0:
                    flag = False
                    break
            if flag:
                ar.append(cur)
        return ar
