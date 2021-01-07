"""
Title     : 1710. Maximum Units on a Truck
Category  : Greedy
URL       : https://leetcode.com/problems/maximum-units-on-a-truck/
Author    : arsho
Created   : 07 January 2021
"""
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        total_boxes = 0
        total_units = 0
        for box_information in boxTypes:
            if total_boxes >= truckSize:
                break
            number_of_boxes, units_per_box = box_information
            if total_boxes + number_of_boxes <= truckSize:
                total_boxes += number_of_boxes
                total_units += number_of_boxes * units_per_box
            elif total_boxes + number_of_boxes > truckSize:
                selected_number_of_boxes = truckSize - total_boxes
                total_boxes += selected_number_of_boxes
                total_units += selected_number_of_boxes * units_per_box
        return total_units
