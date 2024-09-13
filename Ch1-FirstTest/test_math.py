import pytest

#here we have use test_... for function name and if we want we can change to another name to excutes test
def test_one_plus():
    assert 1+5==6

def test_one_plus_two():
    a =1
    b= 2
    c =0
    assert a+b==c

#exception handling
def test_divide_by_zero():
    #this is call pytest.raises and it has predefince expections
    # with : it is commmly used for file input and output
    with pytest.raises(ZeroDivisionError) as e:
      num = 8/0
    assert 'division by zero' in str(e.value)




