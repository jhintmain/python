import re

############## re.DOTALL = re.S : (.)가 줄바꿈 문자를 포함하여 모든 문자와 매치 #############
p = re.compile('a.b')
m = p.match('a\nb')

print(m) # None :ab사이의 \n는 줄바꿈 문자열로 매칭X

p = re.compile('a.b',re.DOTALL)
m = p.match('a\nb')

print(m) # <re.Match object; span=(0, 3), match='a\nb'>     :     ab사이의 \n는 줄바꿈 문자열로 매칭되어야 하지만 re.DOTALL 옵션으로 \n도 포함되게됨


############## re.IGNORECATE = re.I : 대/소문자 구별없이 매치 #############
p = re.compile('[a-z]')
print(p.match('python'))  # 모두 소문자 매칭O
print(p.match('Python'))  # 대문자 P존재 매칭X
print(p.match('PYTHON'))  # 대문자 존재 매칭X

p = re.compile('[a-z]',re.I)
print(p.match('python'))  # 매칭O
print(p.match('Python'))  # 매칭O
print(p.match('PYTHON'))  # 매칭O

############## re.MULTILINE = re.M : 문자열 각 라인을 처음으로 인식 매치 #############
p = re.compile('^python\s\w+') # python으로 문자가 시작하고 뒤에 whitespace가 온후 문자가 나와야한다

data = """python one
life is too short
python two
you need python
python tree"""

print(p.findall(data)) #['python one'] 여러줄이지만 첫문장만 매칭됨

p = re.compile('^python\s\w+', re.M)
print(p.findall(data)) #['python one', 'python two', 'python tree'] 여러줄 모두 매칭됨

############## re.VERBOSE = re.X : 정규식표현내 whitespce 제거해준다,주석(#)포함 #############
p = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);') # 굉장히 복잡한 정규식이다 , 정규식을 가독성좋게 자르고 주석달아주고싶을때

p = re.compile(r"""
&[#]            # Start of a numeric entiry reference
(
    0[0-7]+             # Octal form
   | [0-9]+             # Decital form
   | x[0-9a-fA-F]+      # Hexadecimal form  
)
l
""",re.X)

print(p.match("00x018239df"))



