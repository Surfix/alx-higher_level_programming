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

    def area(self):
        '''calcuate area of a rectangle'''
        return self.width * self.height

    def display(self):
        '''to print string rep of a rectangle'''
        rep = '\n' * self.y + \
              (' ' * self.x + '#' * self.width + '\n') * self.height
        print(rep, end='')

    def __str__(self):
        '''str info about a rectangle'''
        return '[{}] ({}) {}/{} - {}/{}'. \
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def update(self, *args, **kwargs):
        """Update rectangle using arg-var."""
        if args and len(args) > 0:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.width = v
                elif i == 2:
                    self.height = v
                elif i == 3:
                    self.x = v
                elif i == 4:
                    self.y = v
        else:

            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        '''dictionary rep of a class'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
