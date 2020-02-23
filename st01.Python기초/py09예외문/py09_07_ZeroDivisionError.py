num1 = input("숫자1 입력: ")
num2 = input("숫자2 입력: ")

try:
    num1 = int(num1)
    num2 = int(num2)
except ValueError as ex:
    print(ex)

res = num1/num2
