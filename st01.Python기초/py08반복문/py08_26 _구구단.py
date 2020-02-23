
x = input("시작 단수를 입력하세요: ")
x = int(x)

y = input("종료 단수를 입력하세요: ")
y = int(y)

sum = 0

while True:

    if x <= 0 or y <= 0:
        break

    if x < y:
        x = x
        y = y

    else:
        temp = x
        x = y
        y = temp

    for 단 in range(x, y+1, 1):
        for 곱 in range(1, 10, 1):
            str = "%2s * %s = %3s" % (단, 곱, 단*곱)
            if 곱 == 9:
                print(str, end=".")
            else:
                print(str, end=",")


print()  # 줄바꿈
