class MyDB:
    def __init__(self):
        self.connection = Connection()

    def connect(self, connection_string):
        return self.connection

class Connection:
    def __init__(self):
        self.cur = Cursor()

    def cursor(self):
        return self.cur

    def close(self):
        pass

class Cursor():
    def execute(self, query):
        if query == "select id from employee_db where name=vinay":
            return 123
        elif query == "select id from employee_db where name=john":
            return 789
        else:
            return -1

    def close(self):
        pass
