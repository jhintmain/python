# 0~9의 모든 숫자를 각가 한번씩만 사용했는지 확인하는 함수

input_str = input("입력 : ")
input_arr = input_str.split(" ")

for num in input_arr : 
    set_num = set(num)
    if len(num) == 10 and len(set_num) == 10: 
        print("True", end = " ")
    else :
        print("False", end = " ")