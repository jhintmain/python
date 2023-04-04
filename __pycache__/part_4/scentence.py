jumin = "931119-2221222"

print("성별:"+jumin[7])
print("년:"+jumin[0:2])
print("월:"+jumin[2:4])
print("일:"+jumin[4:6])

print("생년월일:"+jumin[:6])
print("뒤 7자리:"+jumin[7:])
print("뒤 7자리:"+jumin[-7:])

python = "Pyhon is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))
print(python.count("n"))    # n이 몇번 나오나

index = python.index("n")
print(index)

index = python.index("n", index+1)
print(index)

find = python.find("n")
print(find)

find = python.find("Java")
print(find) #   -1 이 나옴

index = python.index("Java")
print(index) # Error 