def compute():
    #    ans = max(i * j
    #            for i in range(100, 1000)
    #            for j in range(100, 1000)
    #            if str(i * j) == str(i * j)[ : : -1])
    #    return str(ans)
    m = 0; 
    lst = []
    for i in range(100,1000):
        for j in range(100,1000):
            pr = i* j 
            if (str(pr) == str(pr)[ : : -1]) and pr > m:
                m = pr
                lst.append((i,j,pr))
    print(str(m))
    print(lst)
if __name__ == "__main__":
        print(compute())
