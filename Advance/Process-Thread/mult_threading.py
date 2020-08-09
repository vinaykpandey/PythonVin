import time
import threading
'''
Multithreadin is useful in web services
'''

def cal_square(NList):
    for i in NList:
        time.sleep(1)
        s = i*i
        print("\n")
        print('square of ', i  , ' is : ' , s)


def cal_cube(NList):
    for i in NList:
        time.sleep(1)
        c = i*i*i
        print("\n")
        print('cube of ' , i , ' is : ' , c)


NumberList = [2,3,4,5,6,7]

t1 = threading.Thread(target=cal_square, args=(NumberList,))
t2 = threading.Thread(target=cal_cube, args=(NumberList,))

t1.start()
t2.start()

t1.join()
t2.join()
