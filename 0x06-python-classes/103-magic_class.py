#!/usr/bin/python3
"""Defines a MagicClass class."""


class MagicClass:
    """Represents a magic class."""
    
    def __init__(self, radius=0):
        """Initializes the magic class."""
        self.radius = 0
    
    def area(self):
        """Calculates the area."""
        return self.__radius ** 2 * math.pi
    
    def circumference(self):
        """Calculates the circumference."""
        return 2 * math.pi * self.__radius
