print("종료하려면 음수를 넣으세요 :")

sum = 0
count = 0


while True:  # 무한루프
    입력 = input("성적을 입력하시오: ")
    입력 = int(입력)

    if 입력 < 0:
        break
    else:
        count = count + 1

    sum = sum + 입력

평균값 = sum/count
str = "성적의 평균은 %s 입니다" % 평균값

print(str)
