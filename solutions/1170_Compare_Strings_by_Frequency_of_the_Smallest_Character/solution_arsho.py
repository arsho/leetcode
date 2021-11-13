'''
Title     : 1170. Compare Strings by Frequency of the Smallest Character
Category  : String
URL       : https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
Author    : arsho
Created   : 04 October 2019
'''
from typing import List
import string


class Solution:
    def get_smaller_frequency(self, word: str, letters: str) -> int:
        for letter in letters:
            occurrences = word.count(letter)
            if occurrences > 0:
                return occurrences

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> \
            List[int]:
        letters = string.ascii_lowercase
        result = []
        frequencies = []
        for word in words:
            word_smaller_frequency = self.get_smaller_frequency(word, letters)
            frequencies.append(word_smaller_frequency)

        for query in queries:
            query_smaller_frequency = self.get_smaller_frequency(query,
                                                                 letters)
            temp = list(
                filter(lambda x: x > query_smaller_frequency, frequencies))
            result.append(len(temp))
        return result


if __name__ == "__main__":
    solution = Solution()
    input_arr_1 = ["cbd"]
    input_arr_2 = ["zaaaz"]
    expected_output = [1]
    output = solution.numSmallerByFrequency(input_arr_1, input_arr_2)
    assert output == expected_output, input_arr_1

    input_arr_1 = ["bbb", "cc"]
    input_arr_2 = ["a", "aa", "aaa", "aaaa"]
    expected_output = [1, 2]
    output = solution.numSmallerByFrequency(input_arr_1, input_arr_2)
    assert output == expected_output, input_arr_1
