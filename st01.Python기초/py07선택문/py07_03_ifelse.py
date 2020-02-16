# "grade 가 60보다 크면 "합격입니다."  를 출력합니다.
# 아니면 "불합격입니다." 출력합니다.

grade = input("성적을 입력하시오 :")
grade = int(grade)

if grade > 60:
    print("합격")
else: 
    print("불합격")


정수 = input("정수를 입력하시오.")
정수 = int(정수)
홀짝체크 = 정수%2

if 홀짝체크 == 0 :
    print("입력된 정수는 짝수입니다.")

else:
    print("입력된 정수는 홀수입니다.")

print("종료")