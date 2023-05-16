# 일반 유닛
class Unit:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp

# 공격유닛
class AttackUnit(Unit) :
    def __init__(self,name,hp,dmg):
        # self.name = name
        # self.hp = hp
        Unit.__init__(self,name,hp)
        self.dmg = dmg

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다 [공격력 {}]"\
            .format(self.name, location,self.dmg))

    def damaged(self, dmg):
        print("{} : {} 데이지를 입었습니다".format(self.name, dmg))
        self.hp -= dmg
        print("{} : 현재 체력은 {}입니다". format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다".format(self.name))

class Flyable:
    def __init__(self,speed):
        self.speed = speed
    
    def fly(self, name, location):
        print("{}유닛이 {} 방향으로 날아갑니다 [속도{}]"\
            .format(name,location, self.speed))

# 다중상속
class FlayableAttacUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, dmg, speed):
        AttackUnit.__init__(self,name,hp,dmg)
        Flyable.__init__(self,speed)

valkyrie = FlayableAttacUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name, "3시")

# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)
            


# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5)
# tank = Unit("탱크",150,35)

# wraith1 = Unit("레이스",80,5)
# print("유닛 이름:{} , 공격력{}".format(wraith1.name, wraith1.dmg))

# wraith2 = Unit("빼앗은 레이스",80,5)
# wraith2.clocking= True
# if wraith2.clocking == True:
#     print("{}는 현재 클로킹 상태 입니다".format(wraith2.name))

