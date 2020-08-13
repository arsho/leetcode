"""
Title     : 1286. Iterator for Combination
Category  : Design
URL       : https://leetcode.com/problems/iterator-for-combination/
Author    : arsho
Created   : 13 August 2020
"""
from itertools import combinations


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinations = list(combinations(characters, combinationLength))
        self.combinations_length = len(self.combinations)
        self.iterator_position = 0

    def next(self) -> str:
        word = "".join(self.combinations[self.iterator_position])
        self.iterator_position += 1
        return word

    def hasNext(self) -> bool:
        return self.iterator_position < self.combinations_length

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
