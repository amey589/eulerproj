count = 0 
mcount = ""
def perm(p,s):
    global count 
    global mcount
    if len(s) == 0 :
        #print(p)
        count = count + 1 
        if count == 1000000:
            mcount = p
    for i in range(len(s)):
        #print("p is {} and s[i] is {}".format(p,s[i]))
        perm(p+s[i],s[:i]+s[i+1:])
perm("","0123456789")
print(mcount)

