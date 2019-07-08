import dis
'''
s = "VINAY"
str = ""
for i in s:
    print('current str ==', str ,' iiii char =====', i)
    str = i + str
    print('new str ==', str)

'''
def reverseWord(ActualString):
    pass
    revString = ''
    maxIndex = len(ActualString)
    for i in range(0, maxIndex):
        #j = maxIndex - i -Programs
        #print('iii===', i ,'jjjj ====', j ,' rev char ==', ActualString[j])
        revString = revString +  ActualString[maxIndex - i -1]
    #print(revString)
    return revString
if __name__ == "__main__":
    Inputword = input("Enter Word: ")
    ReverseStr = reverseWord(Inputword)
    print('Revered word is: ', ReverseStr)
    dis.dis(reverseWord)
