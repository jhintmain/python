
# print("Pyton","Java",sep=",", end="?")
# print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# 시험성정
# scores=  {"수학" : 0, "영어":40, "코딩" : 100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=" : ")

# # 은행
# # 001, 002, 003
# for num in range(1,21):
#     print("대기번호 :",str(num).zfill(3))

# answer = input("아무값이나 입력하세요 : ") # input의 항상str이다
# print("입력하신 값은",answer,"입니다")

# # 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 홍 10자리 공간을 확보
# print("{0: >10}".format(500))
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# print("{0:_<10}".format(500))
# print("{0:_<10}".format(-500))

# 3 자리 콤마
print("{0:,}".format(10000000))
print("{0:+,}".format(10000000))
print("{0:+,}".format(-10000000))

# 3자리 콤마,부호, 자리수 확보
# 빈자리는 ^로 채워주기
print("{0:^<+30,}".format(1000000000000))

# 소수점 출력
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3)) # 소수점 3째 자리에서 반올림하여 2째자리까지 표시

