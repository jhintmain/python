# 숫자를 입력받고 숫자의 총합을 구하는 프로그램 작성(숫자는 콤마로 구분)

input_num_list = input("입력 : ")

num_arr = input_num_list.split(",")

total = 0
for num in num_arr :
    total += int(num)

print(total)

