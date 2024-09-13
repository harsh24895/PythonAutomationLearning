#Here we can filter the test case
#1. ex: to test the specific file just mention this path: python -m pytest Ch1-FirstTest\test_math_markers.py
#2. also we want to execute the special module in the test file: python -m pytest python -m pytest -k one.py::test_one_plus_one
#3. If we want to run specific token with the naming parameters it's using -k: python -m pytest -k one "With File name path"

#another thing to is Markers
# Here we have set the markers for Math and Accumulator in all file for Ch8
# It will filter the math file and accumulator
# But we need to mention the filter in the pytest.ini first then it works
# Another marker is skip
