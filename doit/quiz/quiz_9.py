# sample.txt파일을 읽어 총합과 평균값을 구하고 평균값을 result.txt로 써라
import os

f = open(os.path.dirname(__file__)+"/sample.txt", "r")
scores_list = f.readlines()
f.close()

total = 0
cnt = len(scores_list)

for score in scores_list : 
    total += int(score)


with open(os.path.dirname(__file__)+"/result.txt", "w") as f :
    f.write("평균 : "+str(total/cnt) + " 점")


