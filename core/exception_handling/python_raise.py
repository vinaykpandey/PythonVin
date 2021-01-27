# x = int(input("enter num 1: "))
# y = int(input("enter num 2: "))
# try:
#     z = x / y
#     print("result {}".format(z))
# except ZeroDivisionError:
#     print("Invalid division")
#
# print("End")
#
# x = int(input("enter num 1: "))
# y = int(input("enter num 2: "))
# try:
#     z = x / y
#     print("result {}".format(z))
# except TypeError:
#     print("Invalid type")
# except ZeroDivisionError:
#     print("Invalid division")
#
# print("End")
#
# x = int(input("enter num 1: "))
# y = int(input("enter num 2: "))
# try:
#     z = x / y
#     print("result {}".format(z))
# except TypeError:
#     print("Invalid type")
# finally:
#     print("In Finally")
#
# print("End")
#
#
# x = int(input("enter num 1: "))
# y = int(input("enter num 2: "))
# try:
#     z = x / y
#     print("result {}".format(z))
# except (TypeError, ZeroDivisionError):
#     print("Invalid type or zero division")
# finally:
#     print("In Finally")
#
# print("End")

x = int(input("enter num 1: "))
y = int(input("enter num 2: "))
try:
    z = x / y
    print("result {}".format(z))
except (TypeError, ZeroDivisionError):
    print("Invalid type or zero division")
except:
    print("default exception handler")
else:
    print("No exception rasied")
finally:
    print("In Finally")

print("End")
