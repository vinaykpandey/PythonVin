#/usr/bin/python
i = 0
end = 11
sum = 0
for i in range(i, end):
     if(i%3==0 or i%5==0):
          sum = i+sum
          #print("i===== %s", i)
     else:
            print ("i ====== %s", i)
print("total===== %s",sum)


