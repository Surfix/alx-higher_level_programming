#!/usr/bin/python3
'''Rectangle class module - tests located in tests/test_base.py'''
from models.base import Base


class Rectangle(Base):
    '''my Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''init magic'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''get width of a rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set width of a rectangle'''
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''get height of a rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set height of a rectangle'''
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''get x of a rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        '''set x of a rectangle'''
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''get y of a rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        '''set y of a rectangle'''
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''check the value as int and >= 0'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))
