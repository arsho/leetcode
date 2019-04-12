'''
Title     : 1002. Find Common Characters
Category  : Hash Table
URL       : https://leetcode.com/problems/find-common-characters/
Author    : arsho
Created   : 12 April 2019
'''
import unittest
import string


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        result = []
        occurrences = {}
        letters = string.ascii_lowercase
        for letter in letters:
            min_occurences = 101
            for word in A:
                min_occurences = min(min_occurences, word.count(letter))
            occurrences[letter] = min_occurences
        for letter in letters:
            for i in range(occurrences[letter]):
                result.append(letter)
        return result


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_multiple_occurrences(self):
        # example 1
        input_list = ["bella", "label", "roller"]
        output_list = ["e", "l", "l"]
        assert self.solution.commonChars(input_list) == output_list

    def test_white_bishops_all_side(self):
        # example 2
        input_list = ["cool", "lock", "cook"]
        output_list = ["c", "o"]
        assert self.solution.commonChars(input_list) == output_list


if __name__ == '__main__':
    pass
    # Unit tests are for local testing. Leetcode doesn't support this.
    # Uncomment the following line to test code locally
    # unittest.main()
