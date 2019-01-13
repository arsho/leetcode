'''
Title     : 973. K Closest Points to Origin
Category  : Sort
URL       : https://leetcode.com/problems/k-closest-points-to-origin/
Author    : arsho
Created   : 13 January 2019
'''


class Solution:
    def get_distance_from_origin(self, point, origin=[0, 0]):
        """
        :type point: List[int, int]
        :type origin: List[int, int]
        :rtype: double
        """
        return ((point[0] - origin[0]) ** 2 + (
                point[1] - origin[1]) ** 2) ** 0.5

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        ar = []
        for point in points:
            ar.append([point, self.get_distance_from_origin(point)])
        ar = sorted(ar, key=lambda x: x[1])
        res = []
        for i in range(K):
            res.append(ar[i][0])
        return res
