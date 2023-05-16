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

# 건물
class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        #Unit.__inti__(self,name,hp,0)
        super().__init(name,hp,0)       # self는 없이
        self.location = location
        #pass    # 넘어간다

# 서플라이 디폿
supply_depot = BuildingUnit("서플라이 디폿",500,"7시")

def game_start():
    print("새로운 게임을 시작합니다")

def game_over():
    pass

game_start()
game_over()