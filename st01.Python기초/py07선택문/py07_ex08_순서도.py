a = 1
b = 2
c = a+b

while c < 30:
    temp = a
    a = b
    b = c
    c = a+b

print(c)
