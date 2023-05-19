# 피보나치 n입력받고 n이하의 피보나치 수열 출력하는 함수

def fibo(n) : 
    fibo_list = [0,1]

    while True : 
        num = fibo_list[len(fibo_list)-2]+fibo_list[len(fibo_list)-1]
        if num <= n :
            fibo_list.append(num)
        else :
            break
    
    print(fibo_list)

fibo(13)
