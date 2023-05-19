# 한줄 구구단

input_dan = input("구구단을 출력할 숫자를 입력하세요 (2~9) : ")

for i in range(1,10) : 
    print(int(input_dan)*i, end = " ")
    