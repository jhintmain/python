class Unit :
    def __init__(self):
        print("생성자")

class Flyable : 
    def __init__(self):
        print("Flayble 생성자")

class FlyableUnit(Unit,Flyable):
    def __init__(self):
        # super().__init__()  # 다중상속시 맨 처음 클래스만 호출된다.
        Unit.__init__(self)
        Flyable.__init__(self)


dropship = FlyableUnit()