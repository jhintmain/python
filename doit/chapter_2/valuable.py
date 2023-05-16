# 나눗셈
# print(14/3) # 몫이 나오는게 아니라 나눈값이 전체 나온다 > php랑 다룸
# print(14//3) # 몫 : 4
# print(14%3) # 나머지 : 2

# 문자열 표현 방법
# print("문자열 표현-1")
# print('문자열 표현-2')
# print("""문자열 표현-3""")
# print('''문자열 표현-4''')

############################ 문자열 연산

# 1. 문자열 더하기(연결)
# head = "Pyhton"
# tail = " is fun!"
# print(head+tail)

# # 2. 문자열 곱하기(반복)
# print(head*2)

# # 3. 문자열 길이
# print(len(head))

# # Quiz - 1 . You need python 문장의 길이
# quiz_1 = "You need python"
# print(len(quiz_1))

############################ 문자열 인덱싱
# word = "Life is too short, You need Python"
# print(word[0]) # word 0번째 index 글자 : L
# print(word[2]) # word 2번째 index 글자 : f

# print(word[-0]) # word[0]과 같음 : L
# print(word[-2]) # 뒤에서 2번째 글자 : o

############################ 문자열 슬라이싱
# word = "Life is too short, You need Python"
# print(word[0:4]) # word 0~3번째 index까지 문자  : Life
# print(word[:4]) # word 처음부터~3번째 index까지 문자  : Life

# print(word[8:]) # word 10번째 index부터 끝까지 : too short, You need Python

# print(word[19:-7]) # word 19번째 index부터 뒤에서 7번째 문자까지 : You need
# print(word[:])  # 처음부터 끝까지 : Life is too short, You need Python

############################ 문자열 바꾸기
# word_python = "Pithon"
# Pithon > Python으로 바꾸려할때  word_python[1] = y라고 하면??
# 에러남 ,Why? 문자열으 요솟값은 바꿀 수 없기 때문에 ( immutable 자료형)
# 따라서, 문자열을 슬라이싱하여 병합하여 새로운 문자열을 만들어서 작업해야함


############################ 문자열 포맷팅
# 방법 1 . %s /$c / %d / %f 사용하기
# print("I eat %d apples" % 3)
# print("I eat %s apples" % "five")
# print("I eat %d apples. so I was sick for %s days" % (3,"five"))

# 방법 2. format() 함수 사용하기
# print("I eat {0} apples".format(3))
# print("I eat {0} apples. so I was sick for {1} days".format(3,"five"))

# print("I eat {number} apples".format(number = 3))
# print("I eat {number} apples. so I was sick for {day} days".format(number = 3,day="five"))
# print("I eat {0} apples. so I was sick for {day} days".format(3,day="five"))

# print("{0:0.4f}".format(3.1415978)) # 소수점 4번째 자리까지 표기

# 방법 3. 파이썬 3.6부터 f문자 포매팅
name = "코난"
job = "탐정"
print(f"내이름은 {name}! {job}이죠!")

d = {'name':name, 'job':job}
print(f"내이름은 {d['name']:<10}! {d['job']}이죠!")