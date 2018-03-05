class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left<=right:
            mid = (left + right) // 2
            total = (mid*(mid+1))//2
            if total>n:
                right = mid - 1
            elif total<n:
                left = mid + 1
            else:
                return mid
        return right
