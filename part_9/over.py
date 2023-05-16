class Unit:
    def __init__(self,name,hp, speed,damage):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.damage = damage

    def move(self,location):
        print("[지상유닛 이동]")
        print("{}:{} 방향으로 이동합니다.[속도{}]"\
            .format(self.name, location,self.speed))

class AttackUnit(Unit):
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed,damage)


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


# vulture = Unit("벌쳐",80,10,20)
# vulture.move("6시")

# battlecruiset = FlayableAttacUnit("배틀크루저",500,25,3)
# battlecruiset.move("9시")

