'''
Title     : 821. Shortest Distance to a Character
Category  : String
URL       : https://leetcode.com/problems/shortest-distance-to-a-character/
Author    : arsho
Created   : 17 January 2019
'''


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        prev_pos = None
        res = []
        l = len(S)
        for i, v in enumerate(S):
            cur = S[i]
            if cur == C:
                prev_pos = i
                res.append(0)
                continue
            diff = 10 ** 9
            if prev_pos != None:
                diff = i - prev_pos
            try:
                next_pos = S[i + 1:l].index(C)
                diff = min(diff, 1 + next_pos)
            except:
                pass
            res.append(diff)
        return res
