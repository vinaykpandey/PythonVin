class NumberNotInRange(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
          number -- input number which caused the error
          message -- explanation of the error
    """

    def __init__(self, number, message="Number not in range"):
        self.number = number
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "{} -> {}".format(self.number, self.message)


num = int(input("Enter number: "))
try:
    if not 500 < num < 1500:
        raise NumberNotInRange(num)
except NumberNotInRange as N:
    print("{}".format(N.message))
else:
    print("{} is in range".format(num))
finally:
    print("{} is in finally".format(num))
