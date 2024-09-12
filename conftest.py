import pytest

from stuff.accum import Accumulator

#the Fixture has the unique name as a new method name
# the fixture will also do the setup + Cleanup using the yield Statement
#before the yield statment are called Setup steps
#after the yield statement are called cleanup steps

@pytest.fixture
def accum():
    yield Accumulator()

@pytest.fixture
def accum2():
    return Accumulator()