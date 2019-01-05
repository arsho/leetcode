'''
Title     : 551. Student Attendance Record I
Category  : String
URL       : https://leetcode.com/problems/student-attendance-record-i/
Author    : arsho
Created   : 05 January 2019
'''


class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count("A")<=1 and s.count("LLL")<1

if __name__ == '__main__':
    s1 = "PPALLP"
    e1 = True
    s2 = "PPALLL"
    e2 = False
    assert Solution().checkRecord(s1) == e1
    assert Solution().checkRecord(s2) == e2
