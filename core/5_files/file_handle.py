"""
handle a file with keyword "with"
with open ("path", "mode") as FH: don;t need to close()
check if file is closed: FH.closed // This will return True (if closed )/ False (not closed)
"""
import csv
import io


def file_write(file_name, string_to_write):
    fobj = open(file_name, "a")
    fobj.write(string_to_write)
    fobj.write("\n")
    fobj.close()


def reading_csv(file_name):
    f = open(file_name, 'rt')
    try:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            print(type(row))
    finally:
        f.close()


if __name__ == '__main__':
    # file_write('1.csv', "'x','y','z'")
    reading_csv('1.csv');
