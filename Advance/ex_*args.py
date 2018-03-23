'''
def <func-name> (arguments):
    <statements>
'''
def add(*Num):  # this are varibale number of argument, its converted all variables in tuples
    print Num  # this is tuple
    print (type(Num))
    print sum(Num)  #  operator on tuples


add(1,3,5,7)
