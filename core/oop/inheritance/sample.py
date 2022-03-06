class A:
    def __init__(self):
        self.a = 10

    def run_a(self):
        print("Hello A run")
        self.hello_b()

    def hello_b1(self):
        print("Hello A ")


class B(A):
    def __init__(self):
        self.b = 20

    def hello_b(self):
        print("Hello B ")


obj = B()
print("obj: ", obj)
print(obj.__dict__)
obj.run_a()
