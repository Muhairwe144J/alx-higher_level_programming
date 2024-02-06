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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2
