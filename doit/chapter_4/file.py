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