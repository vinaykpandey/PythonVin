class A:
	def __init__(self):
		print("This is class A")

	def abc(self):
		print("AAAAAAAA")


class B:
	def __init__(self):
		print("This is class B")

	def abc(self):
		print("BBBBBBB")

class C(A, B):
	def __init__(self):
		# print("This is class C")
		super().__init__()


obj = C()
# obj.abc()