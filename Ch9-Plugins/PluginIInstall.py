# First of all we need to install the plugins

#use pip3 first then pip if it doesn't work the pip3
# 1.pip3 install pytest-html / if need to uninstall anything just mention pip3 uninstall pytest-html
# Then we can create the report: python -m pytest --html=report.html : this will create a report in the project and we can see
# 2.coverage plugin we install first: pip3 install pytest-cov
# 2.1: Here are things to make sure about that it will show coverage report: python -m pytest --cov=stuff --cov-report.html
# Also check: python -m pytest --cov=stuff --cov-branch

#3. pip3 install pytest-xdist
# python -m pytest -n 3 : this will run three parallel test

#4.pytest-BDD (Behavior-Driven Development)