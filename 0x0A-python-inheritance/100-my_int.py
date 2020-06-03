#!/usr/bin/python3
""" Documentation """


class MyInt(int):
    """class integer """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
