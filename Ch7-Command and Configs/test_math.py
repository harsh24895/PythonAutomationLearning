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


#lession 7-Command and configs
# To run a test here in Terminal we are using command : python -m pytest
#Verbose: python -m pytest --verbose :This will print data /in detail compare to -m pytest
#Quiet: python -m pytest --quiet
#exitfirst: python -m pytest --exitfirst :this is for as soon as first failure happens pytest stops
# junit xml report: python -m pytest --junit-xml xyz.xml :THis will create junit xml file
#pytest.ini: file formate for configuration file format and it's most common. Iff= we crate pytest.ini file in that just mention-
#the test case it will run all the test in verbose or quiet mode.


