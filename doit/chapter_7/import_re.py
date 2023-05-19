import re # 정규식 지원 모듈

p = re.compile('[a-z]+') # 정규식 생성

############## re.math(str) : 문자열 처음부터 정규식과 매치되는지 조사 #############
m = p.match("")
print(m) # None

m = p.match("python")
print(m) # <re.Match object; span=(0, 6), match='python'>


## math의 함수 ##
# group() : 매치된 문자열 return
# start() : 매치된 문자열 시작 index
# end()   : 매치된 문자열 끝 index
# span()  : 매치된 문자열 (시작,끝) 튜플 return


print(m.group())
print(m.start())
print(m.end())
print(m.span())

#### 일반적인 사용방법
if m : 
    print('Match found: ',m.group())
else : 
    print('No math')


############## re.search(str) : 문자열 전체 정규식과 매치되는지 조사 #############
m = p.search("")
print(m) # None

m = p.search("3 python")
print(m) # <re.Match object; span=(2, 8), match='python'>

############## re.findall(str) : 정규식과 매치되는 모든 문자열을 list로 return #############
result = p.findall("Life is too short")
print(result) # ['ife', 'is', 'too', 'short']

############## re.finditer(str) : 정규식과 매치되는 모든 문자열을 반복가능한 객체로 return #############
result = p.finditer("Life is too short")
print(result) # ['ife', 'is', 'too', 'short']
for r in result : print(r)
# <re.Match object; span=(1, 4), match='ife'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>
