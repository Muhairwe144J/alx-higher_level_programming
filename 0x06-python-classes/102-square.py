#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""
    
    def __init__(self, size=0):
        """Initializes the square."""
        self.size = size
        
    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2
    
    def __eq__(self, other):
        """Checks if two squares have the same area."""
        return self.area() == other.area()
    
    def __ne__(self, other):
        """Checks if two squares have different areas."""
        return self.area() != other.area()
    
    def __lt__(self, other):
        """Checks if one square has a smaller area than the other."""
        return self.area() < other.area()
    
    def __le__(self, other):
        """Checks if one square has a smaller or equal area than the other."""
        return self.area() <= other.area()
    
    def __gt__(self, other):
        """Checks if one square has a greater area than the other."""
        return self.area() > other.area()
    
    def __ge__(self, other):
        """Checks if one square has a greater or equal area than the other."""
        return self.area() >= other.area()
