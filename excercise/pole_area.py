import itertools

'''
we have to calculate area created by pole & string
poles are arranged in random order the difference between 2 pole is 1 (unit)
we have to tied a string between 2 poles under some condition:
Pole1 tied with pole longer than pole in sequence
OR
Pole1 is maxmium than all, tied string with local maxima for the remaining pole

Repeat this process and calculate sum of area (i.e. square/rectangle)

'''


#Hlist = [22,19,30,21,24,35,28,23,25,17,12]
#TempList = Hlist

HL = [11,12,13,14,15,16,17,18,19]
iterator = HL.__iter__()
iterator.next()
exit(0);
for x in range(len(HL)):
    print('x ====', x ,' value ===', HL[x])
    if(x == 2):
        x = 5
        iterator.next()
        print(' x jumped from 2 to 5')
