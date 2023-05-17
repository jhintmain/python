# set : 중괄호{}로 감싼다. v2.3부터 지원시작. > why? 집합 관련처리 쉽게하려고
# set의 특징 
# 1. 중복x
# 2. 순서x

s1 = set([1,2,3])
print(s1) # {1,2,3}

s1 = set("Hello")
print(s1) # {'e', 'o', 'l', 'H'} > l은 중복으로 1개만 나옴


s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합
print(s1 & s2) # {4,5,6}
print(s1.intersection(s2)) # {4,5 ,6}
print(s2.intersection(s1)) # {4,5,6}

# 합집합
print(s1 | s2) # {1,2,3,4,5,6,7,8,9}
print(s1.union(s2)) # {1,2,3,4,5,6,7,8,9}
print(s2.union(s1)) # {1,2,3,4,5,6,7,8,9}

# 차집합
print(s1 - s2) # {1,2,3}
print(s1.difference(s2)) # {1,2,3}

print(s2 - s1) # {7,8,9}
print(s2.difference(s1)) # {7,8,9}

# set 함수

# a.add(x) : 1개 값 추가하기
s1 = set([1,2,3,4,5,6])
s1.add(7)
print(s1) # {1,2,3,4,5,6,7}

# a.update(x) : 여러개값 추가하기
s1.update([8,9])
print(s1) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# a.remove(x) : x값 제거
s1.remove(8)
print(s1) # {1, 2, 3, 4, 5, 6, 7, 9}