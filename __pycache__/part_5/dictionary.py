cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100]) # [] Erorr
print(cabinet.get(3))    # get Non
print(cabinet.get(5, "사용가능"))

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet["C-30"]= "조세호"
print(cabinet)
cabinet[3] = "김종국"
print(cabinet)

# 삭제
del cabinet["C-30"]

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

#key-val 출력
print(cabinet.items())

cabinet.clear()
print(cabinet)