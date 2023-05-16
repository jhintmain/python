# 문자열 관련 함수
str = "hobby"

# 문자열내 특정 문자 갯수
print(str.count('b'))

# 문자열내 특정문자 위치알려주기 
# 1. find : 못찻으면 -1 반환
print(str.find('b'))
print(str.find('P'))

# 2. index  :못찻으면 Error 반환
print(str.index('b'))
# print(str.index('P'))

# 소문자 / 대문자 바꾸기
print(str.upper())
print(str.lower())

# 문자열 삽입
print(",".join(str))
print(",".join(['a','b','c','d']))

# 좌/우/좌우 공백 삭제
str = "  moon  "
print(str.lstrip()+"[end]")
print(str.rstrip()+"[end]")
print(str.strip()+"[end]")

# 문자열 바꾸기
str = "Life is too short Life"
print(str.replace("Life", "You Leg")) # 모든 문자열이 바뀜

# 문자열 나누기
print(str.split())
print(str.split("too"))
