
try : 
    # 4/0
    a = [1,2]
    print(a[2])
# except ZeroDivisionError as e : 
#     print(e)
# except IndexError as e : 
#     print(e)

except (ZeroDivisionError, IndexError) as e : 
    print(e)
except FileNotFoundError : 
    pass # 오류 그냥 넘길수도 있음
finally : 
    print('무조건 찍는다')


##### 사용자 Error Class 정의
class MyError(Exception) : 
    def __str__(self):
        return "사용자 정의 error"
    

try : 

    raise MyError("????")
except MyError as e : 
    print(e)

