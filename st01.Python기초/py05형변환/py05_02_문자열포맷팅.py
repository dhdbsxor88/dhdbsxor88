# %s 문자열 혹은 임의의 객체를 문자열로 변환한다. 
# %d 10진 정수로 변환한다. 

# 문자열 포매팅
print("I eat %d apples." %3) 

day = "three"
print("I was sick for %s days." %day)

# 정렬과 공백 (자주 사용함)
print("%10s" %"hi")    #10칸 띄고 입력
print("%-10sjane" %"hi")  #입력하고 10칸

# 소수점 표현
print("%0.4f"%3.42134234)  #소수점 4자리까지 표현
