class A:
    def __init__(self):
        print("This is class A")

    def fn_abc(self):
        print("AAAAAAAA")


class B:
    def __init__(self):
        print("This is class B")

    def fn_abc(self):
        print("BBBBBBB")


class C(A, B):
    def __init__(self):
        # print("This is class C")
        """constructor  of A called"""
        super().__init__()


class D(B, A):
    def __init__(self):
        # print("This is class C")
        """constructor  of B called"""
        super().__init__()


class E(A, B):
    def __init__(self):
        print("This is class E")
        super(self).__init__()
        # B.__init__(self)
        # A.__init__(self)
        # super(B).__init__() # Its not working


# obj_c = C()
# obj_c.fn_abc()
# obj_d = D()
obj_d = E()
