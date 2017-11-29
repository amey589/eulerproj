a = 0
b = 1
c = 0
index = 1
while True:
    c = a + b
    index = index + 1 
    a = b 
    b = c
    if len(str(c)) == 1000:
        break

print(index)

