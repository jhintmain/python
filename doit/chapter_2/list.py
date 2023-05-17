# list  : 대괄호[]로 감싸고, 리스트는 어떠한 자료형도 포함 시 킬수 있다

a = []
b = [1,2,3]
c = ['Life','is','too','short']
d = [1,2,'Life','is']
e = [1,2, ['Life','is']]

print(a)
print(b)
print(c)
print(d)
print(e)

[a2,b2] = ['python','study']
print(a2)
print(b2)

# list 슬라이싱
print(b[0]+b[1]) # 1+2 = 3

# list안에 List접근시
print(str(e[0])+"__"+e[2][0]) # 1__Life

# list 슬라이싱
print(d[:3]) # [1, 2, 'Life'] 

# list 연산하기
# + (더하기)
a = [1,2,3]
b = [4,5,6]
print(a+b)  # [1, 2, 3, 4, 5, 6]

# * (반복하기)
print(a*3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# list 길이 구하기 : len()
print(len(a)) # 3


# 리스트 수정
a = [1,4,3]
a[1] = 2
print(a) #[1, 2, 3]

# 리스트 삭제 : del(x)
a = [1,2,3]
del a[1]
# del a[:]
print(a) # [1, 3]
print(a[1]) # 3

# 그외 list 관련 함수

# append(x) : 마지막에 요소 추가
a = [1,2,3]
a.append(4)
print(a) # [1, 2, 3, 4]
a.append([5,6]) #[1, 2, 3, 4, [5, 6]]
print(a)


# sort() : 정렬
a = [1,3,2]
a.sort()
print(a) # [1, 2, 3]

# reverse() : 뒤집기
a = [1,2,3]
a.reverse()
print(a) # [3, 2, 1]

# index(x) : 위치반환
a = [1,2,3]
print(a.index(3)) # 3이있는 index 위치 반환 없으면 Error

# insert(x, add) : x 번째 index에 add를 추가
a =[1,3,4]
a.insert(1,2)
print(a) # [1,2,3,4]

# remove(x) : 처음으로 나오는 x를 삭제
a = [1,2,3,1,2,3]
a.remove(3)
print(a) # [1,2,1,2,3]

# pop() : 마지막 요소 return해주고 삭제
a = [1,2,3]
last_list = a.pop()
print(last_list) # 3
print(a) # [1,2]

# count(x) :  list내 x의 갯수
a = [1,1,2,3]
print(a.count(1)) # 2

# extend(x_list) : x_list는 list의 형태만 올 수 있으며, 기존리스트뒤에 리스트를 연결 시킨다 (+와 동일한 역할)
a = [1,2,3]
a.extend([4,5])
print(a) # [1,2,3,4,5]
b = [1,2,3]
print(b+[4,5]) # [1,2,3,4,5]

