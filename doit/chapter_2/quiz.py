# Q1. 홍길동씨 평균점수
print("Q1. 홍길동씨 평균점수 : ",end=" ")

q1_ko = 80
q1_en = 75
q1_math = 55

q1_avg = (q1_ko+q1_en+q1_math)/3
print(q1_avg)


# Q2. 자연수 13이 홀수인지 짝수인지 판별할수있는 방법
print("Q2. 자연수 13이 홀수인지 짝수인지 판별할수있는 방법 : 2로나눈 나머지가 0이면 짝,1이면 홀",end=" ")
print(13%2 == 0)

# Q3. 881120-1068234를 나누어 출력해보자
print("Q3. 881120-1068234를 나누어 출력해보자")
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# Q4. 881120-1068234 에서 성별을 나타내는 숫자 출력
print("Q4. 881120-1068234 에서 성별을 나타내는 숫자 출력 ")
print(pin[7])

# Q5. a:b:c:d 문자열을 replace를 사용하여 a#b#c#d로 바꿔보자
print("Q5. a:b:c:d 문자열을 replace를 사용하여 a#b#c#d로 바꿔보자")
q5_str = "a:b:c:d"
print(q5_str.replace(":","#"))

# Q6. [1,3,5,4,2] 리스트를 [5,4,3,2,1]로 만들어보자
print("Q6. [1,3,5,4,2] 리스트를 [5,4,3,2,1]로 만들어보자")
q6_list = [1,3,5,4,2]
q6_list.sort()
q6_list.reverse()
print(q6_list)

# Q7. ['Life','is','too','short'] 리스트를 문자열로 만들어 보자
print("Q7. ['Life','is','too','short'] 리스트를 문자열로 만들어 보자")
q7_list =['Life','is','too','short']
print(" ".join(q7_list))


# Q8. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어보자
print("Q8. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어보자")
# q8_tuple = list((1,2,3))
# q8_tuple.append(4)
# print(tuple(q8_tuple))
q8_tuple = (1,2,3)
q8_tuple = q8_tuple + (4,)


# Q9. a = dict() 라고할때 오류가 발생하는 코드는?
print("Q9. a = dict() 라고할때 오류가 발생하는 코드는?")
# 3번 a[[1]] = 'python' > why? 딕셔너리의 key는 immutable값이 여야 한다. [1]은 list로 변하는 값


# Q10. a = {'A':90,'B':80,'C':70} 일때 result 값
print("Q10. a = {'A':90,'B':80,'C':70} 일때 result 값")
a = {'A':90,'B':80,'C':70} 
result = a.pop('B')
print(a)
print(result)

# Q11. a리스트에서 중복 숫자 제거
print("Q11. a리스트에서 중복 숫자 제거")
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

# Q12. a,b 변수를 선언후 a의 두번째 요소값을 변경하면 b의값은? 결과에 대한 이유는
print("Q12. a,b 변수를 선언후 a의 두번째 요소값을 변경하면 b의값은? 결과에 대한 이유는?")
a = b = [1,2,3]
a[1] = 4
print(b)

print("b도 [1,4,3]으로 된다. a와 b는 같은 메모리를 가리키고 잇기 때문에")
