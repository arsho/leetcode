"""
Title     : 1773. Count Items Matching a Rule
Category  : Array
URL       : https://leetcode.com/problems/count-items-matching-a-rule/
Author    : arsho
Created   : 01 March 2021
"""


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str,
                     ruleValue: str) -> int:
        total_matched_rules = 0
        criteria = ["type", "color", "name"]
        for item in items:
            for i in range(3):
                if criteria[i] == ruleKey and item[i] == ruleValue:
                    total_matched_rules += 1
        return total_matched_rules
