# 기본값 설정 가능 , 중간에끼면 에러남 뒤쪽에다가 선언해야함
def add(a=2, b=4) :
    return a*b

val = add()
print(val) # 8

val2 = add(4,4)
print(val2) # 16

##########################################################
# 입력값이 몇개일지 모를때

def add_many(*args) :
    result = 0
    for num in args : 
        result += num
    return result

print(add_many(1,2,3,4,5)) # 1+2+3+4+5 = 15

##########################################################
# ** 매개변수 dictionary 만들기

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1) # {'a': 1}

print_kwargs(name='foo',age=3) # {'name': 'foo','age':3}

##########################################################
# 함수의 return값은 언제나 1개

def add_and_mul(a,b):
    return a+b, a*b # return이 2개인것처럼 보이지만 , 튜플형태로 1개 return값이다(7,12)

result = add_and_mul(3,4)
a,b = add_and_mul(3,4)
print(result) # (7, 12)
print(a) # 7
print(b) # 12



##########################################################
# lambda : def와 동일한 기능

def add(a,b) :
    return a+b
######################
add = lambda a,b : a+b
