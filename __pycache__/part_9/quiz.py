class House :
    def __init__(self,location,house_type, deal_type, price, year) :
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.year = year
    
    def show_detail(self):
        print("{} {} {} {} {} ".format(self.location,self.house_type,self.deal_type,self.price,self.year))


hosue = []
house1 = House("강남","아파트","매매","10억","2010년")
house2 = House("마포","오피스텔","전세","5억","2007")
house3 = House("송파","빌라","월세","500/50","2000년")

hosue.append(house1)
hosue.append(house2)
hosue.append(house3)

print("총{}대의 매물이 잇습니다".format(len(hosue)))
for info in hosue:
    info.show_detail()

