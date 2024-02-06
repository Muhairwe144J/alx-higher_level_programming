#!/usr/bin/python3


class MagicClass:
    
    def __init__(self, radius=0):
        self.radius = 0
    
    def area(self):
        return self.__radius ** 2 * math.pi
    
    def circumference(self):
        return 2 * math.pi * self.__radius
