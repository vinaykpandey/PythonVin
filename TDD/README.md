Python Testing Framework
    unittest
    nose
    pytest
 
pytest is most recommended

prefix: test_ (infile name as well function name)
test discovery rule
python -m pytest
python -m pytest -v
py.test
py.test -v
pytest -v -rxs 

pytest filename 
pytest filename -v


pytest -k multiply # function based



-------------------------
fixers
---
database related testing
two ways:
1. setup and teardown methods (classic xunit style)
    def setup():
        #database setup connection
    def teardown():
        # after test cases do some cleanup (closed database connection)
2. fixtures (recommended)

pytest -v --capture=no

