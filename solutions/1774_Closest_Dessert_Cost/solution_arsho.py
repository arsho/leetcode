"""
Title     : 1774. Closest Dessert Cost
Category  : Greedy
URL       : https://leetcode.com/problems/closest-dessert-cost/
Author    : arsho
Created   : 05 March 2021
"""
from itertools import combinations
from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int],
                    target: int) -> int:
        toppings = []
        for i in toppingCosts:
            for j in range(2):
                toppings.append(i)

        toppings = sorted(toppings)
        baseCosts = sorted(baseCosts)

        closest_target = None
        for base_cost in baseCosts:
            if closest_target == None:
                closest_target = base_cost
            elif abs(base_cost - target) < abs(closest_target - target):
                closest_target = base_cost
            elif abs(base_cost - target) == abs(closest_target - target):
                closest_target = min(base_cost, closest_target)
            if base_cost >= target:
                break
            d = {}
            for i in range(1, len(toppings) + 1):
                topping_groups = combinations(toppings, i)
                for topping_group in topping_groups:
                    if topping_group not in d:
                        d[topping_group] = True
                        topping_total = sum(topping_group) + base_cost
                        if abs(topping_total - target) < abs(
                                closest_target - target):
                            closest_target = topping_total
                        if abs(topping_total - target) == abs(
                                closest_target - target):
                            closest_target = min(topping_total, closest_target)
        return closest_target
