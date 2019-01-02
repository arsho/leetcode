'''
Title     : 832. Flipping an Image
Category  : Array
URL       : https://leetcode.com/problems/flipping-an-image/
Author    : arsho
Created   : 02 January 2019
'''


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(A)
        m = len(A[0])
        for i in range(n):
            for j in range((m + 1) // 2):
                A[i][j], A[i][m - j - 1] = 1 - A[i][m - j - 1], 1 - A[i][j]
        return A


if __name__ == '__main__':
    A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    B = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    EXPECTED_B = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
    print(Solution().flipAndInvertImage(B))
