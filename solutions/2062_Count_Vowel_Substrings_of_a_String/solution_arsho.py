"""
Title     : 2062. Count Vowel Substrings of a String
Category  : Hash Table
URL       : https://leetcode.com/problems/count-vowel-substrings-of-a-string/
Author    : arsho
Created   : 15 November 2021
"""


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0
        vowels = 'aeiou'
        for i in range(len(word) - 4):
            if word[i] in vowels:
                j = i + 1
                d = {word[i]: 1}
                while j < len(word) and word[j] in vowels:
                    d[word[j]] = 1
                    if sum(d.values()) == 5:
                        count += 1
                    j += 1
        return count
