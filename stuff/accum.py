class Accumulator:

    def __init__(self) -> None:
        self._count = 0 #_count variable called as a private as we seeing single underscore _count

    @property #decorator this will set the get and set method
    def count(self) -> int: #this method get the value of count and couldn't set the value
        return self._count

    def add(self,more=1) -> None:
        self._count += more