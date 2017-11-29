import math
for i in range(1,1000):
    for j in range(1,1000):
        if (i + j + math.sqrt(i*i + j*j) == 1000):
            print("a {} b {} c {}".format(i,j,math.sqrt(i*i+j*j)))
            print(i*j*math.sqrt(i*i+j*j))
            exit(1)


