# abs(x)  : 절대값
print("# abs(x)  : 절대값")
print(abs(-2))
print()

# all(x) : 반복가능한 x인자를 받고, 모든값이 참이면 True
print("# all(x) : 반복가능한 x인자를 받고, 모든값이 참이면 True")
print(all([1,2,3]))
print(all([1,2,False]))
print()

# any(x) : 반복가능한 x인자를 받고, 하나라도 참이면 True
print("# all(x) : 반복가능한 x인자를 받고, 하나라도 참이면 True")
print(any([1,2,3]))
print(any([1,2,False]))
print()

# chr(i) : 아스키코드값 입력받아 문자출력
print("# chr(i) : 아스키코드값 입력받아 문자출력")
print(chr(97))
print()

# dir(x) : 체가 가지고있는 변수/함수를 보여줌
print("# dir(x) : 체가 가지고있는 변수/함수를 보여줌")
print(dir([1,2,3])) # list가 가지고있는 메소드/변수들
print(dir({1:'a'})) # dictionary 가지고있는 메소드/변수들
print()

# divmod(a,b) : a/b 를 몫/나머지를 tuple로 반환
print(divmod(7,2)) # (3,1)

# *** enumerate(x) : 순서있는 자료형(리스트,튜플,문자열) x인자를 받고 index값을 포함하는 객체로 돌려준다
for i,name in enumerate(['body','foo','var']) : 
    print(i,name)


# eval(expression) : 실행가능한 문자열을 변수로 받아, 문자열을 실행한 결과값을 돌려줌 >> 입력받은 문자열로 함수/클래스를 동적으로 실행하고 싶을때 사요
e1 = eval('1+2')
e2 = eval("'hi' +'a'")
e3 = eval('divmod(4,3)')
print(e1,e2,e3)


# filter(function_name, x) : 객체로 돌려주니 list나 tuple 알맞게 변경해서 뽑아와
def positive(j) : 
    result = []
    for i in j : 
        if i>0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6])) # [1,2,6]

# positive와 같은 역할의 filter
def positive2(x) :
    return x>0

print(list(filter(positive2,[1,-3,2,0,-5,6])))

# 더 업그레이드 함수를 lambda로 표현한 filter
print(list(filter(lambda x: x>0,[1,-3,2,0,-5,6])))


# map(function_name, x) : x값을 function_name한 결과값으로 돌려줌
def double(num_list) : 
    result = []
    for i in num_list : 
        result.append(i*2)

    return result

print(double([1,2,3,4]))

# doble 같은 역할의 map
def doble2(x) :
    return x*2

print(list(map(doble2,[1,2,3,4])))

# 더 업그레이드 함수를 lambda로 표현한 filter
print(list(map(lambda x: x*2,[1,2,3,4])))

# id(object) : object의 고유 주소란을 돌려줌
print(id('12312'))

# int(x,radix=10) : 숫자형으로 표기
print(int('10'))
print(int('11',2))
print(int('1A',16))

# isinstance(object,class) : obejct가 class의 instance인지 체크 True/False

# pow(a,b) : x의 y 제곱

# range(start=0, end, term=1) : term 부분은 start ~ end까지 간격
print(list(range(0,10,2))) # [0, 2, 4, 6, 8]

# round(i,dig=0) : i를 반올림하여 dig자리까지 표기
print(round(4.6)) # 5
print(round(4.66345,2)) # 4.66 까지 표기

