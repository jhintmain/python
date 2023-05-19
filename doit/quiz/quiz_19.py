# 뒷자리 숫자 4개를 ####로 바꾸는 정규식 작성
import re

word = """
park 010-999-8998
kim 010-9909-1234
lee 010-9898-4456
"""

p = re.compile("[0-9]{4}$",re.MULTILINE)
word_change = p.sub('####',word)

print(word)
print(word_change)
