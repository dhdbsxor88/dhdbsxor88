a = input("첫번째수를 입력하세요.")
b = input("두번째수를 입력하세요.")
c = input("세번째수를 입력하세요.")

a = int(a)
b = int(b)
c = int(c)

if a<b and a<c :
    print("가장 작은 수는", a)

elif b<a and b<c : 
     print("가장 작은 수는", b)

else :
    print("가장 작은 수는", c)

  