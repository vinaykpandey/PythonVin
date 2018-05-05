def list_procession(L, inputs):
            if len(inputs)==1:
                command =inputs[0]
            elif len(inputs)==2:
                command = inputs[0]
                e = int(inputs[1])
            elif len(inputs)==3:
                command = inputs[0]
                i = int(inputs[1])
                e = int(inputs[2])
            # process list
            if command=="insert":
                 L.insert(i,e)
            elif command=="remove":
                 L.remove(e)
            elif command=="append":
                 L.append(e)
            elif command=="sort":
                 L.sort()
            elif command=="pop":
                 L.pop()
            elif command=="reverse":
                 L.reverse()
            elif command=="print":
                 print(L)

if __name__ == '__main__':
    N = int(raw_input()) #[Number of operation/iteration]
    #import random
    L= []
    #[iterate number of operation in loop]
    for row in range(N+1):
            #[convert passed value in list]
            inputs = raw_input().split()
            list_procession(L, inputs)
            #print('list elements =====', L)
