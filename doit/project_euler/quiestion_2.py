
import os
now_path = os.path.dirname(__file__)

# 문제 격자 읽기
f = open(now_path+"/q11_source.txt",'r')
f_txt = f.read()
f_txt_arr = f_txt.split("\n")
f.close()

def mul(arr_list):
    if 0 in arr_list : 
        return 0
    else :
        result = 1 
        for num in arr_list : 
            result *= num
        return result

# list로 셋팅
set_arr = []
for a in f_txt_arr : 
    tmp = a.split(" ")
    tmp_arr = [int(x) for x in tmp]
    set_arr.append(tmp_arr)

# print(set_arr)
n = 4
max = 0

# 세로 : 0,0 ->0,1
print("세로")
for j , set_j in enumerate(range(len(set_arr[0]))) :
    # print(j)
    for i, set_i in enumerate(range (len(set_arr)-n+1))  :
        cal_mul = mul(set_arr[i][j:j+n])
        if max < cal_mul : 
            # print(set_arr[i][j:j+n])
            max = cal_mul  
# 가로
print("가로")
for i , set_i in enumerate(range(len(set_arr))) :
    # print(i)
    for j, set_j in enumerate(range (len(set_arr[i])-n+1))  :
        cal_mul = mul(set_arr[i][j:j+n])
        if max < cal_mul : 
            # print(set_arr[i][j:j+n])
            max = cal_mul
        
# 오른쪽 대각선 : (0,0)(1,1)(2,2)(3,3) / (0,1)
print("오른쪽 대각선")
for i in range(len(set_arr)-n+1): # 0~16 
    for j in range(len(set_arr)-n+1): # 0~16 
        llist = []
        for z in range(4) : 
            # print(i+z,end=" ")
            # print(j+z,end=" ")
            llist.append(set_arr[i+z][j+z])
        
        # print(llist)
        cal_mul = mul(llist)
        if max < cal_mul : 
            print(llist)
            max = cal_mul

print("왼쪽 대각선") # (0,19)~ (3,16)
for i in range(len(set_arr)-n+1): # 0~16 
    for j in range(len(set_arr)-1,n-2,-1): # 19~3
        llist = []
        for z in range(4) : 
            print(i+z,end=" ")
            print(j-z,end=" ")
            llist.append(set_arr[i+z][j-z])
        
        print(llist)
        cal_mul = mul(llist)
        if max < cal_mul : 
            print(llist)
            max = cal_mul

    



print(max)