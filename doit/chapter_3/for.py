
# 표현 1
a_list = ['one','two','three']

for i in a_list : 
    print(i)


# 표현 2
b_list = [(1,2),(3,4),(5,6)]

for (first,last) in b_list : 
    print(first+last)

# 같이 자주쓰는 range(0,11) 
for i in range(0,11) : # 0~10까지
    print(i,end=",")

print()

for i in range(11) : # 0~10까지
    print(i, end=",")


# 구구단
print ()
for i in range(2,10):
    for j in range(1,10) : 
        print (i*j, end=" ")
    print ()

# 리스트 내표하기
a = [1,2,3,4]
result = []

# 방법 1
for num in a :
    result.append(num*3)

# 방법 2
result2 = [num * 3 for num in a]

print(result) # [3,6,9,12]
print(result2) # [3,6,9,12]


# 짝수만 담고 싶다
result3 = [num * 3 for num in a if num%2 == 0]
print(result3)


# 리스트 내표에서 for문 2개도 가능하다
# ex 구구단
result4 = [x*y for x in range(2,10)
        for y in range(1,10)]
print(result4)