# x = int(input("enter num 1: "))
# y = int(input("enter num 2: "))
# try:
#     if y == 0:
#         # this will call constructor of class ZeroDivisionError(built-in class)
#         raise ZeroDivisionError("denominator can not be zero")
#     z = x/y
# except ZeroDivisionError: # dev Handle machanism
#     print("you can not divide by zero")

class InsufficientBalance(ZeroDivisionError):
    def __init__(self, arg):
        self.message = arg


balance = 500
w = int(input("enter amount to withdraw: "))
try:
    if w > balance:
        raise InsufficientBalance("you have less amount")
    balance = balance - w
except InsufficientBalance as I:
    print("InsufficientBalance", I.message)
else:
    print("withdrawl amount successfully", w)
finally:
    print("current balance: ", balance)
