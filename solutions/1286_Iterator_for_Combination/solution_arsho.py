"""
Title     : 1286. Iterator for Combination
Category  : Design
URL       : https://leetcode.com/problems/iterator-for-combination/
Author    : arsho
Created   : 13 August 2020
"""


class CombinationIterator:

    def __init__(self, characters: str, combination_length: int):
        self.characters = characters
        self.combinations = self.get_combinations(characters,
                                                  combination_length)
        self.total_combinations = len(self.combinations)
        self.iterator_position = 0

    def next(self) -> str:
        word = self.combinations[self.iterator_position]
        self.iterator_position += 1
        return word

    def hasNext(self) -> bool:
        return self.iterator_position < self.total_combinations

    def get_combinations(self, characters, valid_length) -> list:
        combinations = []
        total_characters = len(characters)
        max_bit = (2 ** total_characters) - 1
        for i in range(max_bit, -1, -1):
            binary_presentation = str(bin(i))[2:].zfill(total_characters)
            if binary_presentation.count("1") == valid_length:
                word = ""
                for j in range(total_characters):
                    if binary_presentation[j] == "1":
                        word += characters[j]
                combinations.append(word)
        return combinations

"""
Using combinations method from itertools package
"""
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
"""