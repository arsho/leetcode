class Solution:
    def climbStairs(self, n: int) -> int:
        res = []
        res.append(1)
        res.append(1)
        for i in range(n + 1):
            res.append(res[-1] + res[-2])
        return res[n]