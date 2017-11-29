import math
def check_prime(n):
    is_prime = True
    for i in range(2,int(math.sqrt(n)+1)):
        if (n % i == 0):
            is_prime = False
            break
    return is_prime

def get_nth_prime(n):
    i = 2
    pcount = 0
    while(True):
        if(check_prime(i)):
            pcount = pcount + 1 
        print("i is {} pcount is {} check_prime ans is {} ".format(i,pcount,check_prime(i)))
        if (pcount == n):
            return i
        i = i+ 1 
print(check_prime(4))
print(get_nth_prime(10001))
