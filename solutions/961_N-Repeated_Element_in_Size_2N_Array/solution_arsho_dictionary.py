class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A) // 2

        d = {}
        for i in A:
            d[i] = d.get(i, 0) + 1
            if d[i] == n:
                return i

# Runtime: 120 ms
