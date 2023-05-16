# input
# language = input("무슨언어 좋아하세요?")
# print(f"{language}는 아눚 좋은 언어 입니다!")

# dif
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())

# print(dir(random))


# lst = [1,2,3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))


# glob : 경로 내의 폴더  파일 목록 조회( 윈도우 dir )
# import glob
# print(glob.glob("*.py"))

# # os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리
# folder = "sample_dir"
# if os.path.exists(folder):
#     print("already exists")
#     os.rmdir
#     print("folder delete")
# else : 
#     os.makedirs(folder)
#     print(folder, "folder make success")
# print(os.listdir())

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("today date :", datetime.date.today())

# timedelta : 두 날짜 사이간격
today = datetime.date.today()  # 오늘 날짜
td = datetime.timedelta(days=100) # 100일 저장
print("today we met 100 :  ",today+td)