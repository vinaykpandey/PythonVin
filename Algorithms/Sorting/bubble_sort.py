def bubuleSort(Nlist):
    print('original list', Nlist)
    n = len(Nlist)
    #traversed through list element
    for i in range (1):
        #print (i,'----', Nlist[i])
        #Last i elements are already in place
        swapFlag = False
        for j in range(0,n-i-1):
            print('i = ',i,' , j = ',j)
            #print (j)
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            swapFlag = False
            if(Nlist[j] > Nlist[j+1]):
                print('values ', Nlist[j],'==Swap==', Nlist[j+1])
                Nlist[j] , Nlist[j+1] =  Nlist[j+1], Nlist[j]
                swapFlag = True
            else:
                print('---No---')
            print(Nlist)
        if(not swapFlag):   # to reduce number of iteration
            print('break');
            break;
    print(' sorted list ',Nlist)
# Driver code to test above
#listN = [64, 34, 25, 12, 22, 11, 90]
listN = [5, 3, 1, 9, 8, 2, 4, 7]
bubuleSort(listN)
