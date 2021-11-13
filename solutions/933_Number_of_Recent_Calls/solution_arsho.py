'''
Title     : 933. Number of Recent Calls
Category  : Queue
URL       : https://leetcode.com/problems/number-of-recent-calls/
Author    : arsho
Created   : 17 January 2019
'''


class RecentCounter(object):

    def __init__(self):
        self.pings = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.pings.append(t)
        min_value = t - 3000
        valid_pings = list(filter(lambda x: x >= min_value, self.pings))
        self.pings = valid_pings
        return len(valid_pings)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
