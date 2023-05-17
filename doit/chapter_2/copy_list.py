a = [1,2,3]
b = a
print(b) # [1,2,3]

# 이렇게 하면 a = b와 완전 동일 같은id값을 참고하고 잇기에 b가 바뀌면 a도 바뀐다(반대도 같음)
print(str(id(a))+"__"+str(id(b)))



# 리스트를 복사하는 방법 2가지
# 1. [:] 사용
a = [1,2,3]
b = a[:]
a[0] = 4
print(a) # [4, 2, 3]
print(b) # [1, 2, 3]


# 2. copy 모듈 사용
from copy import *
a = [1,2,3]
b = copy(a)
a[0] = 4
print(a) # [4, 2, 3]
print(b) # [1, 2, 3]

# 두변수 바꾸기
a = '3'
b = '5'
print(a+"_"+str(id(a))) # 3
print(b+"_"+str(id(b))) # 5

a,b = b,a
print(a+"_"+str(id(a))) # 5
print(b+"_"+str(id(b))) # 3
