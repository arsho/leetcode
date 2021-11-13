'''
Title     : 1160. Find Words That Can Be Formed by Characters
Category  : Hash Table
URL       : https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
Author    : arsho
Created   : 27 September 2019
'''
from typing import List


class Solution:

    def word_to_dict(self, word):
        d = {}
        for char in word:
            d[char] = d.get(char, 0) + 1
        return d

    def countCharacters(self, words: List[str], chars: str) -> int:
        d = self.word_to_dict(chars)
        count = 0
        for word in words:
            e = self.word_to_dict(word)
            can_create_word = True
            for c in e:
                if d.get(c, 0) < e[c]:
                    can_create_word = False
                    break
            if can_create_word:
                count += len(word)
        return count


if __name__ == "__main__":
    solution = Solution()
    words = ["hello", "world", "leetcode"]
    chars = "welldonehoneyr"
    expected_answer = 10
    given_answer = solution.countCharacters(words, chars)
    assert expected_answer == given_answer, \
        "{},{}".format(expected_answer, given_answer)

    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    expected_answer = 6
    given_answer = solution.countCharacters(words, chars)
    assert expected_answer == given_answer, \
        "{},{}".format(expected_answer, given_answer)
