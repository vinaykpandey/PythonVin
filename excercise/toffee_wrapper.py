"""
amount
toffee rate; number(s) of toffee per ruppee
toffee = amount*toffee rate
rapper = toffee
again; extra toffee with rapper: > rapper rate = number of rapper per toffee
extra toffee =  rapper//rapper rate
total toffe = toffee + extra toffee
"""
amount = int(input("Enter amount: "))
toffee_rate = int(input("Enter the rate for toffee i.e. number of toffees per ruppee: "))
rapper_rate = int(input("Enter rapper rate i.e. number of rapper per toffee: "))
toffee = amount * toffee_rate
rapper = toffee  # initial value of rappers
while rapper >= rapper_rate:
    extra_toffee = rapper // rapper_rate
    toffee = toffee + extra_toffee
    rapper = extra_toffee + rapper % rapper_rate  # Value assigned after each iteration
print("Total toffee in ruppees {} are {}.".format(amount, toffee))
print("Remaining rapper are {}.".format(rapper))