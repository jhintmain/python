# 홀수가 연속 (-), 짝수가 연속(*)를 붙여서 return
input_str = input("입력 : ")

for i in range(len(input_str)) :
    b_num = int(input_str[i])

    if i == 0 :
        a_num = b_num
    else :
        if a_num%2 == b_num%2 : 
            if b_num%2 == 0 : 
                print("*",end="")
            else : 
                print("-",end="")
        a_num = b_num
    # 4546793
    print(b_num,end="")






    

