class SoldOutError(Exception):
    def __init__(self) :
        pass

chicken = 10
waiting = 1
while(True):
    print(f"[남은치킨 : {chicken}]")
    
    try:
        if chicken <= 0 :
            raise SoldOutError
        else  :
            order = int(input("주문할 치킨수 : "))
            
            if order < 1 :
                raise ValueError
            elif chicken < order:
                print("재료부족")
            else:
                print(f"[대기번호 {waiting}] {order} 마리 주문 완료")
                waiting += 1
                chicken -= order
    except ValueError : 
        print("잘못된 값을 입력하였습니다")
    except SoldOutError as err : 
        print("재고가 소진되어 더이상 주문을 받지않습니다")
        break
    
