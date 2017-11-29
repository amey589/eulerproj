import math
def find_all_divisors(n):
    divisor_count = 0
    for i in range(2,int(math.sqrt(n))):
        if n %i == 0 :
            divisor_count = divisor_count + 1
    return divisor_count*2 + 2
def get_triangle_num(num):
    sm = 0 
    for i in range(0,num+1):
        sm = sm + i 
    return sm

num = 1
tr_num = 0 
while(True):
    tr_num = num + tr_num
    #print(tr_num," ",end=" ")
    divisors = find_all_divisors(tr_num)
    #print(divisors)
    if find_all_divisors(tr_num) > 500:
        print(tr_num)
        exit(1)
    num = num + 1 
#print(find_all_divisors(6))
