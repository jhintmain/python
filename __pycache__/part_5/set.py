# set{} : 중복 x, 순서x
my_set = {1,2,3,4,4,4}
print(my_set)

java = {"우재석","홍길동","김산아"}
python = set(["우재석","박명수"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java-python)
print(java.difference(python))

python.add("김태호")
print(python)

java.remove("김산아")
print(java)
