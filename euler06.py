import math
def sum_of_squares(n):
    ans = 1 
    for i in range(2,n+1):
        ans = ans + i*i
    return ans 
def square_of_sums(n):
    ans = 1
    for i in range(2,n+1):
        ans = ans + i 
    return ans*ans
#print(sum_of_squares(10))
#print(square_of_sums(10))
print(square_of_sums(100) - sum_of_squares(100))

