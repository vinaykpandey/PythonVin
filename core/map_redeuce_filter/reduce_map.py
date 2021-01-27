import time
from multiprocessing import Pool

'''
Its uses the core of CPU,  
reduce map is make sense when we have more than 1 cpu
'''

def f(n):
    return n*n

if __name__ == "__main__":
    p = Pool(processes=3)

    '''
    p.map(fuction name, argument pass i.e. list in this case)
    '''
    result = p.map(f,[1,2,3,4,5])
    for n in result:
        print(n)
