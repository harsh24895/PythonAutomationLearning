import pytest

#multiplication ideas:
#two positive number
#idetify:multiply by 1
#zero: multiply by 0
#positive to negative
#negative to positive
#floats

#Here we have created a tuple
products =[
    (5,6,30),
    (45,75,78),
    (5,45,69),
    (4,-7,-7),
    (-8,-5,9),
    (5.5,6.8,9.2)
]

@pytest.mark.parametrize('a,b,product',products)#this is a decoder function which wraps around another function below
#And this is helpful if we want to take multiple inputs
#here this parameters('a,b,product',products) are from the test_multi function and product are the values
def test_multi(a,b,product):
    assert a*b == product