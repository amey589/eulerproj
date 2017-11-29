import math
n = 1000000;
factors = []
found = False
while (n > 0): 
#    print("n is {}".format(n))
    for i in range(1,int((n/2)+1)):
        #print("i is {} ".format(i))
        if n%i == 0 :
            tup = (i,n/i)
            #factors.append((i,n/i))
            if( ((tup[0]>99) and (tup[0]<1000)) and
                ((tup[1]>99) and (tup[1]<1000)) and
                (str(n) == "".join(list(reversed(str(n)))))):
                found = True
                break
    if (found):
        print("found number with two three digit factors")
        print("tuple is {}".format(tup) )
        break
    n = n-1 ; 
print("loop ended")

