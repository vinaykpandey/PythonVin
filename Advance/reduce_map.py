import time
from multiprocessing import Pool


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
