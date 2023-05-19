# Calculator 클래스 작성

class Calculator : 
    def __init__(self,args) :
        self.args = args

    def sum(self) : 
        result = sum(self.args)
        print (result)
        return result
    
    def avg(self) : 
        result = self.sum()/len(self.args)
        print(result)
        return result


cal1 = Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()

cal2 = Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()

