def fact(n):
    ans = 1 
    while (n > 1):
        ans = ans * n 
        n = n - 1 
    return ans
a = fact(10)
print(a)
print(sum(int(i) for i in list(str(a))))
