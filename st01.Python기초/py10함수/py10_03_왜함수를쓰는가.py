
# 1부터 10까지의 합계를 구하고
# 그 합계를 sum에 저장하고 sum 값을 한번만 출력한다.

# 1부터 100까지의 합계를 구하고
# 그 합계를 sum2 에 저장하고 sum2 값을 한번만 출력한다.

# 100부터 sum2까지의 합계를 구하고
# 그 합계를 sum3 에 저장하고 sum3 값을 한번만 출력한다.

sum = 0

for x in range(1, 11, 1):
    sum = sum + x

print(sum)

sum2 = 0

for x in range(1, 101, 1):
    sum2 = sum2 + x

print(sum2)

sum3 = 0

for x in range(100, sum2+1, 1):
    sum3 = sum3 + x

print(sum3)


# 반복 코드를 함수를 만들어 사용
# 바뀌는 값은 입력(매개변수)으로 처리

def get_sum(z, y):
    sum3 = 0

    for x in range(z, y, 1):
        sum3 = sum3 + x

    print(sum3)

    return sum3


# 함수 호출 = 함수 사용

sum1 = get_sum(1, 1)  # 1부터 10까지의 합계를 구하고 출력
sum2 = get_sum(1, 100)
sum3 = get_sum(100, sum2)
