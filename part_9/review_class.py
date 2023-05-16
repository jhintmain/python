from random import *
class Unit : 
    def __init__(self, name,hp,dmg=0,speed = 0):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.speed = speed

        print(f"[{name}]유닛이 생성되었습니다")
        print(f"체력 : {hp} , 공격력 : {dmg}, 속도 : {speed}")

    def move(self,location):
        print(f"{self.name} : {location} 방향으로 이동합니다 [속도{self.speed}]")

    def damaged(self,dmged):
            print(f"{self.name} : {dmged} 데미지를 입었습니다.")

            self.hp-=dmged

            if self.hp <=0:
                print(f"{self.name} : 현재체력은 0 입니다")
                print(f"{self.name} : 파괴되었습니다.")
            else :
                print(f"{self.name} : 현재체력은 {self.hp} 입니다")



# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5)

# lays1 = Unit("레이스",80,5)
# lays2 = Unit("레이스",80,5)
# lays1.clooking = True
# if lays1.clooking == True :
#     print("lays1은 클로킹 상태 입니다")


class AttackUnit(Unit) :
    def __init__(self,name,hp,dmg,speed):
        Unit.__init__(self,name,hp,dmg,speed)

    def attack(self,location):
        print(f"{self.name} : {location} 방향으로 공격합니다[공격력{self.dmg}]")


class Marine(AttackUnit):
    def __init__(self) :
        AttackUnit.__init__(self,"마린",40,1,5)

    def stimpack(self):
        if self.hp>10:
            self.hp-=10
            self.dmg+=10
            print(f"{self.name} : 스팀팩을 사용합니다 *HP 10 감소")
        else :
            print(f"{self.name} : 체력이 부족하여 스팀팩을 사용할 수 없습니다")
            

class Tank(AttackUnit):
    seize_developed = False
    
    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,10,35)
        self.seize_mode = False

    def set_seize_mode(self):
        if self.seize_developed == False :
            return
        else :
            if self.seize_mode == False:
                print(f"{self.name} : 시즈모드로 전환합니다")
                self.dmg*=2
                self.seize_mode = True
            else :
                print(f"{self.name} : 시즈모드를 해제합니다")
                self.dmg/=2
                self.seize_mode = False





# firebat1 = AttackUnit("파이어뱃", 50,16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

            
class Flyable :
    def __init__(self,fly_speed) :
        self.fly_speed = fly_speed

    def fly(self,name,location) :
        print(f"{name} : {location} 방향으로 날아갑니다 [속도{self.fly_speed}]")
    

class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,dmg,fly_speed):
        AttackUnit.__init__(self,name,hp,dmg,0)
        Flyable.__init__(self,fly_speed)

    def move(self,location):
        self.fly(self.name,location)

# valkyrie = FlyableAttackUnit("발키리",200,6,5)
# valkyrie.fly(valkyrie.name,"3시")

# virture = AttackUnit("벌쳐",80,10,20)
# battlecruiser = FlyableAttackUnit("배틀크루저",500,25,3)

# virture.move("11시")
# battlecruiser.move("11시")


class Race(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",80,20,5)
        self.clocked = False

    def clocking(self):
        if self.clocked == False :
            print(f"{self.name} : 클로킹 모드로 전환합니다")
            self.clocked = True
        else :
            print(f"{self.name} : 클로킹 모드를 해제합니다")
            self.clocked = False            



class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        # pass

        Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0)

        self.location = location


def game_start():
    print("[알림] 새로운 게임을 시작합니다")

def game_over():
    print("[gg]")

def unit_move(units, location):
    for unit in units :
        unit.move(location)

def unit_attack(units, location):
    for unit in units :
        unit.attack(location)

def unit_damaged(units):
    for unit in units :
        unit.damaged(randint(5,51))

############################## 게임시작
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Race()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

unit_move(attack_units, "1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다")


for unit in attack_units : 
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit,Race) :
        unit.clocking()


unit_attack(attack_units, "1시")

unit_damaged(attack_units)

game_over()