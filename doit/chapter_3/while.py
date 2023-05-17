
coffe = 10
while True : 
    money = int(input("돈을 넣어주세요"))
    if money == 300 : 
        print("커피를 줍니다")
        coffe -= 1
    elif money > 300 : 
        print(f"거스름돈{money-300}을 주고 커피를 줍니다")
        coffe -=1
    else : 
        print("돈을 돌려주고 커피를 주지않음")
        print(f"남은 커피양은{coffe}개 입니다")
    
    if coffe == 0 : 
        print("커피가 다 떨어졌어요 판매중지")
        break