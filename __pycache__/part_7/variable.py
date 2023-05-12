# gun = 10

# def checkpoint(soldiers) :
#     global gun
#     gun = gun - soldiers
#     print("[함수내] 남은 총 : {}".format(gun))

# def checkpoint_ret(gun, soliers):
#     gun = gun-soliers
#     print("[함수내] 남은 총 : {}".format(gun))
#     return gun

# print("전체 총 : {}".format(gun))
# checkpoint(2)
# print("남은 총 : {}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {}".format(gun))


import sys

print("Pyhthon", "java", sep=",", end="?")
print("Python", "Java",file=sys.stdout)
print("Python", "Java",file=sys.stderr)

# 시험 성적
scores = {"math":0, "english":50, "coding":100}

for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4),sep=":")

# 대기번호
for num in range(1,21):
    print("waiting number", str(num).zfill(3), sep=":")


# 사용자 입력시 type은 문자열
answer = input("아무값이나 입력하세요")
print(type(answer))
