
pos = 0
value = ""

#  List 선언

리스트 = []


#  C: 추가. 검색: "파이썬 리스트 추가"
#  MILK, BREAD, BUTTER 순으로 추가
#
리스트.append("MILK")
리스트.append("BREAD")
리스트.append("BUTTER")


#  APPLE 삽입. 검색: "파이썬 리스트 삽입"
#  특정 위치에 추가하기
#  "BREAD" 앞에 "APPLE" 삽입
#  "BREAD" 가 들어있는 방번호 찾기


#  R: 읽기
#  BUTTER 값을 출력하시오.
#  "BUTTER" 가 들어있는 방번호 찾기
#

방번호 = 리스트.index("BUTTER")
리스트.insert(방번호, "APPLE")

#  U: 수정. 검색: "파이썬 리스트 수정"
#  "BREAD" 를 "GRAPE"로 변경
#  "BREAD" 가 들어있는 방번호 찾기
#

방번호 = 리스트.index("BREAD")
리스트[방번호] = "GRAPE"


#  D: 인덱스로 삭제. 검색: "파이썬 리스트 삭제"
#  인덱스를 이용하여 GRAPE 를 삭제
#

방번호 = 리스트.index("GRAPE")
리스트.pop(방번호)


#  D: 값으로 찾아서 삭제. 검색: "파이썬 리스트 값으로 삭제"
#  값으로 MILK를 찾아서 삭제하시오
#
리스트.remove("MILK")


#  P: 리스트를 for문으로 출력.
#  검색: "파이썬 리스트 for 출력"
#  검색: "파이썬 리스트 크기"
#

for i in 리스트:
    print(i)

#  P: 리스트를 for-each문으로 출력.
#
for i in range(0, len(리스트)):
    print(i, 리스트[i])


#  테스트용 데이터 생성을 위한 코드. 수정하지 마시오.
for i in range(4):
    리스트.append("APPLE")
    리스트.append("BANNA")

print(리스트)


#  S: 검색: "파이썬 리스트 검색
#  첫번째 APPLE을 찾으시오.
방번호 = 리스트.index("APPLE")
print(방번호)


#  S: 오름차순 정렬. 검색: "파이썬 리스트 오름차순 정렬"
리스트.sort()

print(리스트)
#  S: 내림차순 정렬. 검색: "파이썬 리스트 내림차순 정렬"

리스트.reverse()
print(리스트)

#  검색2. APPLE 이 몇개 있나요?
애플개수 = 리스트.count("APPLE")
print(애플개수)


#  변환된 배열을 for 문으로 출력.
for i in 리스트:
    print(i)


#  list의 모든 값을 while문을 사용하여 삭제하시오
