"""
Fixtures are functions, which will run before each test function to which it is applied.
Fixtures are used to feed some data to the tests such as database connections,
URLs to test and some sort of input data. Therefore, instead of running the same code for every test,
we can attach fixture function to the tests and it will run and return the data to the test
before executing each test.

A function is marked as a fixture by −
@pytest.fixture

pytest -v (for all test case)
pytest -k divisible -v   (for samename testcase)

However, the approach comes with its own limitation. A fixture function defined inside a test
file has a scope within the test file only. We cannot use that fixture in another test file

To make a fixture available to multiple test files, we have to define the fixture function in a file called conftest.py.

"""