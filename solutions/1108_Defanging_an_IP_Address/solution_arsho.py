'''
Title     : 1108. Defanging an IP Address
Category  : String
URL       : https://leetcode.com/problems/defanging-an-ip-address/
Author    : arsho
Created   : 27 September 2019
'''


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
