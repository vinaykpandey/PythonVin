from .db import MyDB
import pytest

@pytest.fixture()
def cur():
    print("**************  START  DB **************")
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    yield curs
    curs.close()
    conn.close()
    print(" ----------- closing DB --------------- ")

def test_vinay_id(cur):
    id = cur.execute("select id from employee_db where name=vinay")
    assert id == 123

def test_john_id(cur):
    id = cur.execute("select id from employee_db where name=john")
    assert id == 789