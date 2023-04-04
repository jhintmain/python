from random import *

class Unit:
    def __init__(self,name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{}유닛이 생성 되었습니다".format(self.name))

    def move(self,location):
        print("{}:{} 방향으로 이동합니다.[속도{}]"\
            .format(self.name, location,self.speed))

class AttackUnit(Unit):
    def __init__(self,name,hp,speed,damage) :
        Unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self,location):
        print("{}:{}방향으로 적군 공격[공격력{}]".format(self.name,location, self.damage))
    
    def damaged(self, dmg):
        print("{} : {} 데이지를 입었습니다".format(self.name, dmg))
        self.hp -= dmg
        print("{} : 현재 체력은 {}입니다". format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다".format(self.name))


class Flyable:
    def __init__(self,fly_speed):
        self.fly_speed = fly_speed

    def fly(self, name, location):
        print("{}유닛이 {} 방향으로 날아갑니다 [속도{}]"\
            .format(name,location, self.fly_speed))

class FlayableAttacUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, fly_speed):
        AttackUnit.__init__(self,name,hp,0, damage)
        Flyable.__init__(self,fly_speed)

    def move(self, location) :
        print("[공중유닛 이동]")
        self.fly(self.name,location)

class Marine(AttackUnit):
    def __init__(self) :
        AttackUnit.__init__(self,"마린",40,1,5)

    def stimpack(self):
        if self.hp>10:
            self.hp -= 10
            print("{}:스팀팩을 사용합니다(HP10 감소)".format(self.name))
        else :
            print("{}:체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))

class Tank(AttackUnit):
    seize_developed = False 

    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.seize_mode = False
        
    def set_seize_mode(self):
        if Tank.seize_developed == False : 
            return  

        if self.seize_mode == False :
            print("{}: 시즈모드로 전환합니다".format(self.name)) 
            self.damage *=2
            self.seize_mode = True
        else : 
            print("{}: 시즈모드를 해제 전환합니다".format(self.name)) 
            self.damage /=2
            self.seize_mode = False

class Wraith(FlayableAttacUnit):
    def __init__(self):
        FlayableAttacUnit.__init__(self,"레이스",80,20,6)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{} : 클로킹모드 해제".format(self.name))
            self.clocked = False
        else :
            print("{} : 클로킹모드 설정".format(self.name))
            self.clocked = True


def game_start():
    print("새로운 게임을 시작합니다")

def game_over():
    print("Player : gg")
    print("[Player] : 님이 게임에서 퇴장하셨습니다")

# 실제게임 진행
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# list로 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크시즈모드 개발이 완료되었습니다")

# 공격 모드 준비( 탱크 : 시즈모드 , 레이스 :클로킹, 마린 :스팀팩)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    else:
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5,21))
game_over()