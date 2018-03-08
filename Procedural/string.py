ActualString = 'VINAY'
revString = ''
maxIndex = len(ActualString)
for i in range(0, maxIndex):
    j = maxIndex - i -1
    print('iii===', i ,'jjjj ====', j ,' rev char ==', ActualString[j])
    revString = revString +  ActualString[maxIndex - i -1]
    print(revString)

s = "VINAY"
str = ""
for i in s:
    print('current str ==', str ,' iiii char =====', i)
    str = i + str
    print('new str ==', str)
