"""
Title     : 1629. Slowest Key
Category  : Array
URL       : https://leetcode.com/problems/slowest-key/
Author    : arsho
Created   : 25 October 2020
"""
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        key_response_time_map = {}
        slowest_time = None
        slowest_key = None
        for i in range(len(releaseTimes)):
            pressed_key = keysPressed[i]
            if i == 0:
                response_time = releaseTimes[0]
            else:
                response_time = releaseTimes[i] - releaseTimes[i - 1]
            current_release = max(key_response_time_map.get(pressed_key, 0),
                                  response_time)
            key_response_time_map[pressed_key] = current_release
            if slowest_time == None or current_release > slowest_time:
                slowest_time = current_release
                slowest_key = pressed_key
            elif current_release == slowest_time and pressed_key > slowest_key:
                slowest_key = pressed_key
        return slowest_key
