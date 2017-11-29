def create_collatz_chain(n):
    tmp = n
    chain_len = 0;
    while(True):
#        print(n) 
        if (n == 1):
            break
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        chain_len = chain_len + 1
    return chain_len+1
mx = 0; 
no = 0
print(create_collatz_chain(13))
for i in range(2,1000000):
    l =  create_collatz_chain(i)
    if (mx < l) :
        mx = l
        no = i
print(mx)
print(no)

