import sys # 파이썬 인터프리터가 제공하는 변수와 함수 직접제어할수있게 해주는 모듈
import pickle # 객체형태 그대로 유지하면서 파일에 저장하고 불러올수있게 해주는 모듈
import os # 환경변수/디렉터리/파일 등의 os자원 제어해주는 모듈

import shutil # 파일 복사해주는 모듈

# 자주 쓰는거 같은거
# os.environ['PATH'] # PATH 변수

# os.chdir('C:/Users/user') # path경로로 현재 디렉토리 위치 변경

# os.getcwd() # 현재 자신의 디렉토리 위치 알려줌

# os.system('dir') # 시스템 명령어 호출 > 현재 디렉토리에서 'dir'명령어 실행

# f = os.popen('dir') # 실행한 시스템 명령어의 결과값 돌려받기(읽기모드 파일형태 객체로 돌려줌)
# print(f.read())



# shutil
shutil.copy("src.txt","dst.txt")