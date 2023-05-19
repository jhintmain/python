# 실행결과 예측하기

result = 0

try:
    [1,2,3][3]
    "a"+1
    4/0
except TypeError: 
    result += 1
except ZeroDivisionError: 
    result += 2
except IndexError: 
    result += 3
finally : 
    result += 4


print(result) # 7

## 답 : 7 IndexError걸리고 이후 Exception은 skip후 finally 실행

