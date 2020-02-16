a = input("첫번째수를 입력하세요.")
b = input("두번째수를 입력하세요.")
c = input("세번째수를 입력하세요.")

a = int(a)
b = int(b)
c = int(c)

if a>b:
    if a>c:
        print(a)
    else:
        print(c)

if a<b:
    if b>c:
        print(b)
    else:
        print(c)

print("입력하신 세 숫자 중 위 숫자가 가장 큰 수 입니다")


a = input("첫번째수를 입력하세요.")
b = input("두번째수를 입력하세요.")
c = input("세번째수를 입력하세요.")

a = int(a)
b = int(b)
c = int(c)

if a>b and a>c : 
    print(a)

elif b>a and b>c :
    print(b)

else : 
    print(c)

print("입력하신 세 숫자 중 위 숫자가 가장 큰 수 입니다")

