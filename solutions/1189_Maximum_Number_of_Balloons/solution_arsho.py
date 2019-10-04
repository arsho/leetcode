'''
Title     : 1189. Maximum Number of Balloons
Category  : Hash Table
URL       : https://leetcode.com/problems/maximum-number-of-balloons/
Author    : arsho
Created   : 02 October 2019
'''


class Solution:
    def word_to_char_dictionary(self, text: str) -> dict:
        d = {}
        for c in text:
            d[c] = d.get(c, 0) + 1
        return d

    def maxNumberOfBalloons(self, text: str) -> int:
        number_of_baloons = 0
        target = "baloon"
        d = self.word_to_char_dictionary(target)
        e = self.word_to_char_dictionary(text)

        return number_of_baloons


if __name__ == "__main__":
    solution = Solution()
    input_str = "nlaebolko"
    result = solution.maxNumberOfBalloons(input_str)
    expected_result = 1
    assert result == expected_result, input_str

    input_str = "loonbalxballpoon"
    result = solution.maxNumberOfBalloons(input_str)
    expected_result = 2
    assert result == expected_result, input_str

    input_str = "leetcode"
    result = solution.maxNumberOfBalloons(input_str)
    expected_result = 0
    assert result == expected_result, input_str
