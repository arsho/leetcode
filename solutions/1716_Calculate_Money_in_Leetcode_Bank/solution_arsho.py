"""
Title     : 1716. Calculate Money in Leetcode Bank
Category  : Greedy
URL       : https://leetcode.com/problems/calculate-money-in-leetcode-bank/
Author    : arsho
Created   : 21 January 2021
"""


class Solution:
    def totalMoney(self, n: int) -> int:
        money = 0

        count_week_day = 1
        current_drop = 1
        while n > 0:
            n -= 1
            money += current_drop
            if count_week_day == 7:
                current_drop -= 5
                count_week_day = 1
                continue
            count_week_day += 1
            current_drop += 1
        return money


if __name__ == "__main__":
    solution = Solution()
    n = 4
    expected_output = 10
    result = solution.totalMoney(n)
    assert result == expected_output, f"Error in {n}, " \
                                      f"expected {expected_output}, " \
                                      f"found {result}"

    n = 10
    expected_output = 37
    result = solution.totalMoney(n)
    assert result == expected_output, f"Error in {n}, " \
                                      f"expected {expected_output}, " \
                                      f"found {result}"

    n = 20
    expected_output = 96
    result = solution.totalMoney(n)
    assert result == expected_output, f"Error in {n}, " \
                                      f"expected {expected_output}, " \
                                      f"found {result}"
