# 정규식 a[.]{3,}b와 매칭되는 문자열
# 답 : acccb

# 다음 코드의 결과괎
import re
p = re.compile("[a-z]+")
m = p.search("5 7 pytho43n")
m.start() + m.end() # 2+7 = 9 
# 2+8 = 10??? 왜지? start는 index 고 end는 자리수인가봄??
