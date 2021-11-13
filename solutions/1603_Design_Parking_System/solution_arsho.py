"""
Title     : 1603. Design Parking System
Category  : Design
URL       : https://leetcode.com/problems/design-parking-system/
Author    : arsho
Created   : 14 May 2021
"""


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.car_slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        carType -= 1
        if self.car_slots[carType] >= 1:
            self.car_slots[carType] -= 1
            return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
