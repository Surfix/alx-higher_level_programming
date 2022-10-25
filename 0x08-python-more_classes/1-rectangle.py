#!/usr/bin/python3

"""Simple Rectangle Module."""


class Rectangle:
    """Represent a Rectangle."""
    def __init__(self, width=0, height=0):
        self.__width =  width
        self.__height = height

    @property
    def width(self):
        """Get value of the width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
