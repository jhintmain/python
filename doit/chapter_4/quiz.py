# Q1
def is_odd(number):
    if number%2 == 0:
        return True 
    else : 
        return False

# Q2
def avg_numbers(*args):
    result = 0
    for i in args : 
        result +=i
    return result/len(args)

a= avg_numbers(1,2)
b= avg_numbers(1,2,3,4,5)
print(a)
print(b)

# Q3
# input1 = int(input("첫번째 수를 입력하세요 : "))
# input2 = int(input("두번째 수를 입력하세요 : "))
# total = input1+input2
# print(total)

# Q4
# 3번 , 로 연결하면 띄어쓰기가 생긴다

# Q5
import os
now_path_full = os.path.dirname(os.path.realpath(__file__)) # 현재 작업중인 프로젝트
f1 = open(now_path_full+"/Q5.txt",'w')
f1.write('Life is too short\nyou need java')
f1.close()

f2 = open(now_path_full+'/Q5.txt','r')
print(f2.read())
f2.close()


# Q6
user_input = input("저장할 내용을 입력하세요 :")
f = open(now_path_full+"/Q6.txt",'w',encoding="UTF-8")
f.write(user_input)
f.write("\n")
f.close()

# Q7
f = open(now_path_full+"/Q5.txt",'r')
body = f.read()
f.close()

body = body.replace("java",'python')

f = open(now_path_full+"/Q5.txt",'w')
f.write(body)
f.close()
# Q8

# Q9

# Q10