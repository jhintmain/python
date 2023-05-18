# 파일생성하기
# f = open("새파일.txt",'w')
# f.close()

# 파일모드 3가지
# r : 읽기모드
# w : 쓰기모드 - 처음부터 다시쓰기
# a : 추가모드 - 파일 마지막에 내용추가

# 파일생성하기
import os
parent_path = os.pardir # ..
cuurent_path = os.curdir # .
work_path_full = os.getcwd() # workspace
now_path_full = os.path.dirname(os.path.realpath(__file__)) # 현재 작업중인 프로젝트

f = open(os.path.join(now_path_full,"새파일.txt"),'w')
f.close()


# 파일만들기 : writedata.py
f = open(os.path.join(now_path_full,"n번째줄.txt"),'w', encoding="UTF-8")

for i in range(1,11):
    data = f"{i}번째 줄입니다\n"
    f.write(data)
f.close()


# 파일읽기 : 3가지 방법
# 1. f.readline() :  한줄씩 읽기
f = open(os.path.join(now_path_full,"n번째줄.txt"),'r', encoding="UTF-8")
while True : 
    line = f.readline()
    if not line : break
    print(line,end="")
f.close()
print()
# 2. f.readlines() : 모든줄을 읽어 list 로 return
f = open(os.path.join(now_path_full,"n번째줄.txt"),'r', encoding="UTF-8")
for line in f.readlines(): 
    print(line, end="")
f.close()
print()
# 3. f.read() : 모든내용을 string으로 return
f = open(os.path.join(now_path_full,"n번째줄.txt"),'r', encoding="UTF-8")
data = f.read()
print(data)
f.close()

# 파일 내용 추가 하기
f = open(os.path.join(now_path_full,"n번째줄.txt"),'a', encoding="UTF-8")

for i in range(11,21):
    f.write(f"{i}번째 줄입니다\n")

f.close()

# with문 사용하기 : with밖으로 나갈때 자동으로 close()해줘서 편리함
with open(os.path.join(now_path_full,"life.txt"),'w') as f : 
    f.write('Life is too short, you need python')
    
