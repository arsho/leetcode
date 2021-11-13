'''
Title     : 852. Peak Index in a Mountain Array
Category  : Binary Search
URL       : https://leetcode.com/problems/peak-index-in-a-mountain-array/
Author    : arsho
Created   : 10 January 2019
'''


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A_length = len(A)
        for i in range(1, A_length):
            if A[i]<A[i-1]:
                return i-1

if __name__ == '__main__':
    a1 = [0,1,0]
    e1 = 1
    assert Solution().peakIndexInMountainArray(a1) == e1

    a1 = [0,2,1,0]
    e1 = 1
    assert Solution().peakIndexInMountainArray(a1) == e1

    a1 = [0,1,2,3,2,1]
    e1 = 3
    assert Solution().peakIndexInMountainArray(a1) == e1
