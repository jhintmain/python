from random import *
winner = range(1,21)
winner = list(winner)
print(winner)

shuffle(winner)
winner = sample(winner,4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winner[0]));
print("커피 당첨자 : {0}".format(winner[1:]));
