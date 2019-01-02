'''
Title     : 942. DI String Match
Category  : Math
URL       : https://leetcode.com/problems/di-string-match/
Author    : arsho
Created   : 02 January 2019
'''


class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        current_max = n
        current_min = 0
        ar = []
        for c in S:
            if c == 'I':
                ar.append(current_min)
                current_min += 1
            else:
                ar.append(current_max)
                current_max -= 1
        missing_value = (n * (n + 1)) // 2 - sum(ar)
        ar.append(missing_value)
        return ar


if __name__ == '__main__':
    S = "IDID"
    print(Solution().diStringMatch(S))
