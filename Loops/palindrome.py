def  Palindrome(s):
        y = s[::-1]
        print (y)
        if s == s[::-1]:
            print ("Palindrome")
        else:
             print ("NOT Palindrome")


        '''length = len(s)
        i = 0
        #while i < length / 2 + 1:
        for i in range(length / 2 + 1):
            if s[i] != s[length-1-i]:
                print "Not Palindrome"
                break
            i += 1
        else:
            print "Palidrome"'''


Palindrome('Vinay')
