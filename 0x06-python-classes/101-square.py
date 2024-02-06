#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square."""
        self.size = size
        self.position = position
        
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
        
    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position
    
    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        
    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2
    
    def my_print(self):
        """Prints the square using # characters."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
            
    def __str__(self):
        """Returns a string representation of the square."""
        square_str = ""
        if self.__size == 0:
            return square_str
        for _ in range(self.__position[1]):
            square_str += "\n"
        for _ in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size + "\n"
        return square_str[:-1]
