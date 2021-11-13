"""
Title     : 705. Design HashSet
Category  : Hash Table
URL       : https://leetcode.com/problems/design-hashset/
Author    : arsho
Created   : 03 August 2020
"""


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def add(self, key: int) -> None:
        self.data[key] = 1

    def remove(self, key: int) -> None:
        if key in self.data:
            del self.data[key]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.data

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
