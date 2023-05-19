# 문자열 압축 , 연속적으로 반복된 숫자의 경우 반복횟수 문자열 출력

# aaabbcccccca
input_str = input("입력 : ")

before_c = input_str[0]
cnt = 0

for now_c in input_str : 
    if before_c == now_c : 
        cnt += 1 
    else :
        print(before_c+str(cnt),end="")
        cnt = 1
    
    before_c = now_c

print(before_c+str(cnt),end="")



    

