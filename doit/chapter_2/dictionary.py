# dictionary : 중괄호{}로 감사고 key:value 쌍이 기본 형태 ( hash 또는 연관배열이라고도 함)

a = {"name" : "jihea", "age" : 31}
b = {3:'0 index', '1' : '1 index'}

print(a)
print(b)

# !! dic에서 중요한것은 a[x] 에서 x가 index가 아닌 key값이라는것 , 문자와 숫자 구분 필수.
print(b[3]) # 0 index
# print(b[1]) #  error > '1'로 써줘야함
print(b['1']) #  1 index

# dic은 중복 불가이다 > 써도 되긴하지만 먼저 선언된 key와 관련된 값은 뒤어 key값으로 덮어써진다.
a = {1:'name',1:'age'}
print(a) # {1,:'age'}

# dic 관련 함수

# a.keys() : key값들만 모아서 dict_keys 객체로 돌려줌
a = {"name" : "jihea", "age" : 31}
print(a.keys()) # dict_keys(['name', 'age'])
print(list(a.keys())) # ['name','age']

# a.values() : value 값만 모아서 dict_values 객체로 돌려줌
print(a.values()) # dict_values(['jihea', 31])
print(list(a.values())) # ['jihea',31]

# a.items() : key-value 쌍을 '튜플'로 묶은 값을 dict_itmes객체로 돌려줌
print(a.items())

# a.clear() : 전체 삭제
a = {"name" : "jihea", "age" : 31}
a.clear()
print(a) # {}

# a.get(key) : key로 value값 얻기
a = {"name" : "jihea", "age" : 31}
print(a.get("name")) # jihea
print(a["name"]) # jihea

print(a.get("job")) # None
# print(a["job"]) # Error

print(a.get("job","programmer")) # programmer ( 기본값 설정 가능 )

# key in a : key가 a dictionary에 존재하는지 확인 ( True/ False)
a = {"name" : "jihea", "age" : 31}
print('name' in a ) # True
print('job' in a ) # False