from collections import Counter


class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A) // 2
        counter = Counter(A)
        for i in A:
            if counter[i] == n:
                return i
# Runtime: 88 ms
