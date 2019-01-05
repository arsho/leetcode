'''
Title     : 896. Monotonic Array
Category  : Array
URL       : https://leetcode.com/problems/monotonic-array/
Author    : arsho
Created   : 05 January 2019
'''


class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        l = len(A)
        if l==1:
            return True
        flag = True
        prev = A[0]
        category = 0
        for i in range(1, l):
            c = A[i]
            if c<prev:
                if category == 0:
                    category = -1
                    prev = c
                    continue
                elif category == 1:
                    return False
            if c > prev:
                if category == 0:
                    category = 1
                    prev = c
                    continue
                elif category == -1:
                    return False
            prev = c
        return True


if __name__ == '__main__':
    a1 = [6, 5, 4, 4]
    s1 = Solution().isMonotonic(a1)
    e1 = True
    assert s1 == e1

    a1 = [1, 2, 4, 5]
    s1 = Solution().isMonotonic(a1)
    e1 = True
    assert s1 == e1

    a1 = [1, 1, 1]
    s1 = Solution().isMonotonic(a1)
    e1 = True
    assert s1 == e1

    a1 = [1, 3, 2]
    s1 = Solution().isMonotonic(a1)
    e1 = False
    assert s1 == e1
