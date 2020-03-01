#####################
# 얕은 복사 vs 깊은 복사
#####################

#####################
# 리스트 복사
#####################

#####################
# 리스트 복제
#####################

array = []

while True:
    i = input("성적을 입력하시오 : ")
    i = int(i)
    if i < 0:
        break
    array.append(i)

k = sum(array)/len(array)

print(k)

print(len(array))
