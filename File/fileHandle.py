#!/usr/bin/env python
'''
handle a file with keyword "with"
with open ("path", "mode") as FH: don;t need to close()
check if file is closed: FH.closed // This will return True (if closed )/ False (not closed)
'''
import csv
import io
def fileWrite(fileName, StringtoWrite):
    fobj  = open(fileName, "a")
    fobj.write(StringtoWrite)
    fobj.write("\n")
    fobj.close()

def readingCsv(fileName):
    f = open(fileName, 'rt')
    try:
        reader = csv.reader(f)
        for row in reader:
            print row
            print(type(row))
    finally:
        f.close()
if __name__ == '__main__':
    #fileWrite('1.csv', "'x','y','z'")
    readingCsv('1.csv');
