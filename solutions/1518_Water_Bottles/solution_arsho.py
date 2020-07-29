"""
Title     : 1518. Water Bottles
Category  : Greedy
URL       : https://leetcode.com/problems/water-bottles/
Author    : arsho
Created   : 29 July 2020
"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drink_bottles = numBottles
        empty_bottles = numBottles
        while True:
            free_bottles = empty_bottles // numExchange
            empty_bottles = empty_bottles - (
                        free_bottles * numExchange) + free_bottles
            total_drink_bottles += free_bottles
            if empty_bottles < numExchange:
                break
        return total_drink_bottles
