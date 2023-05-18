# Q1
class Calculator : 
    def __init__(self) : 
        self.value =0
    def add(self,val) :
        self.value +=val 

class UpgradeCalculator(Calculator) : 
    def minus(self, val) : 
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

# Q2
class MaxLimitCalculator(Calculator):
    def add(self,val) : 
        self.value += val
        if self.value > 100 :
            # print('value가 100이 넘습니다')
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

# Q3. False/ True

# Q4
q4_list = [1,-2,3,-5,8,-3]
# def plus(i) : 
#     if i>0 : 
#         return i
# print(list(filter(plus,q4_list)))

print(list(filter(lambda i : i>0 ,q4_list)))

# Q5 > pass

# Q6
q6_list = [1,2,3,4]

print(list(map(lambda x : x*3, q6_list)))

# Q7
q7_list = [-8,2,7,5,-3,5,0,1]
print(int(max(q7_list))+int(min(q7_list)))

# Q8
print(round(17/3,4))

# Q9
import sys
args = sys.argv[1:]

def list_sum(args) : 
    total =0
    for i in args : 
        total += int(i)

    return total

print(list_sum(args))

# Q10
import os
os.chdir('C:/Users/user/OneDrive/바탕 화면/PythonWorkspace/doit')
f = os.popen('dir')
print(f.read())

# Q11
import glob
q11_list = glob.glob('C:/Users/user/OneDrive/바탕 화면/PythonWorkspace/doit/*.py')
print(q11_list)

# Q12 
import time
print(time.strftime("%Y/%m/%d %H:%M:%S"))
print(time.strftime("%Y/%m/%d %X"))

# Q13
import random

# set을 이용한 방법
random_list = set([])
while len(random_list) < 6 : 
    random_list.add(random.randint(1,45))

# list를 이용한 방법
# random_list = []
# while len(random_list) < 6 : 
#     num = random.randint(1,45)
#     if num not in random_list : 
#         random_list.append(num)

print(random_list)