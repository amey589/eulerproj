import math

def check_prime(n):
    is_prime = True
    for i in range(2,int(math.sqrt(n)+1)):
        if (n % i == 0):
            is_prime = False
            break
    return is_prime


def find_primes_upto(n):
    for i in range(2,n):
        if check_prime(i):
            yield i
s = 0
for i in find_primes_upto(2000000):
    s = s + i
print(s)

