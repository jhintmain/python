# from random import *

# result_passenger = 0

# for passenger in range(1, 51):
#     time = randint(5,50)
#     possible = ' '
#     if 5<=time<=15 :
#         possible = 'o'
#         result_passenger+=1
#     print("[{}] {}번째 손님 (소요시간 : {}분)".format(possible,passenger,time))

# print("총 탑승객 : {} 분".format(result_passenger))

from random import *
passenger = 0

for guest in range(1,51) :
    time = randint(5,50)
    if time>=5 and time<=15:
        able = "O"
        passenger+=1
    else :
        able = "X"
    
    print("[{}] {}번째 손님 (소요시간 : {}분)".format(able, guest,time))

print("총 탑승 승객 : {}분".format(passenger))
