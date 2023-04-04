gun = 10

def checkpoint(soldiers) :
    global gun
    gun = gun - soldiers
    print("[함수내] 남은 총 : {}".format(gun))

def checkpoint_ret(gun, soliers):
    gun = gun-soliers
    print("[함수내] 남은 총 : {}".format(gun))
    return gun

print("전체 총 : {}".format(gun))
checkpoint(2)
print("남은 총 : {}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {}".format(gun))