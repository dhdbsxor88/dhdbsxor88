

def Add(First, Second):
    result = First + Second
    return result


x = input("첫번째 숫자 :")
y = input("두번째 숫자 :")
x = int(x)
y = int(y)
value = Add(x, y)

print(value)
