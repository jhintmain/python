# 자료구조
# list / dictionary / set / tuple

# 1. list []
array_list = [10,20,30,10]

# 2. set {} : 순서x, 중복x
array_set = {10,20,30,10}

# 3. tuple () : 고정 배열
array_tuple = (10,"유재석",20)

# 4. dictionary {key:val}
array_dictionary = {3:"유재석", 100:"김태호"}

print(array_list)
print(array_set)
print(array_tuple)
print(array_dictionary)

transe_list = list(array_set)
print(transe_list)

transe_set = set(array_list)
print(transe_set)

transe_tuple = tuple(array_list)
print(transe_tuple)