import math
def find_divisors(n):
    divisors = [] 
    for i in range(1,n):
        if( n % i == 0 ):
            divisors.append(i)
    return divisors
def is_amicable(n):
   divisors = find_divisors(n)
   sm = sum(divisors)
   #print(sm)
   if sm == n :
       return False
   sm_divisors = find_divisors(sm)
   #print(sm_divisors)
   sm_sm = sum(sm_divisors)
   #print(sm_sm)
   #print("num is {} sum is {}  divisors are {}".format(n,sm,divisors))
   #print("sm is {} sm_sm is {} sm_divisors  are {}".format(sm,sm_sm,sm_divisors))
   if n == sm_sm :
      return True
   return False

sm = 0
#print(is_amicable(220))
for i in range(1,10000):
   if (is_amicable(i)):
       sm = sm + i
       print("amicable no {}".format(i))
print(sm)

    
