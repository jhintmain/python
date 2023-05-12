try :
    print("나누기 전용 계산기 입니다")
    num1 = int(input("첫번째수 : "))
    num2 = int(input("두번째수 : "))
    print(f"{num1} / {num2} = {num1/num2}")

except ValueError : 
    print("에러 잘못된 값 입력")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)
    print("알 수 없는 에러")


1
# 사용자 정의 에러
class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg
    

try:
    print("한 자리 숫자 나눈기 전용 계산기")
    num1 = int(input("첫번째 숫자 :"))
    num2 = int(input("두번째 숫자 :"))

    if num1 >=10 or num2>=10 :
        raise BigNumberError(f"입력값 {num1}, {num2}")
except ValueError : 
    print("잘못된 값 입력")
except BigNumberError as err:
    print("한자리만 입력해주세요")
    print(err)
finally :
    print("계산기 종료")