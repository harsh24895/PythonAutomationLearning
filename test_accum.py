import pytest

from stuff.accum import Accumulator

def test_accumulator_init():
    accum =Accumulator()
    assert accum.count==0

def test_accumulator_add():
    accum = Accumulator()
    accum.add()
    assert accum.count==1 ##this add 1 with no other arguments

def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3) #this will add three to the count as method has been called
    assert accum.count == 3

def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2

def test_accumulator_cannot_set_count_directly():
    accum =Accumulator()
    with pytest.raises(AttributeError, match=r"property 'count'of 'Accumulator' object has no setter") as e:
        accum.count = 10

 #these all pattern are called "Arrange act-assert" called classic three step pattern to test case