"""
Title     : 1436. Destination City
Category  : String
URL       : https://leetcode.com/problems/destination-city/
Author    : arsho
Created   : 04 May 2020
"""
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        final_destination = None
        for path in paths:
            source, destination = path
            d[source] = destination
        for source, destination in d.items():
            final_destination = destination
            while destination in d:
                final_destination = d[destination]
                destination = d[destination]
            return final_destination
