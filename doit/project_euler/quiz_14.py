
import threading
import time

start_time = time.time()
max_dic = {'cnt':0, 'num' : 1000000}

def jobs(start_idx, end_idx) : 
    global max_dic
    print(start_idx)
    max_cnt = 0
    max_num = start_idx

    for i in range(start_idx, end_idx ,-1) : 
        start_num = i
        cnt = 0

        # print(i, end = " : ")
        # print(str(max_cnt),str(max_num))
        while True : 
            if start_num % 2== 0 :
                start_num //= 2 
            else :
                start_num = 3*start_num+1

            cnt += 1

            if start_num == 1:
                break         
        
        if cnt > max_cnt : 
            max_cnt = cnt
            max_num = i
    # return max_cnt, max_num
    if max_dic['cnt'] < max_cnt :
        max_dic['cnt'] = max_cnt
        max_dic['num'] = max_num



# 스레드 생성
threads = []
term = -100000
for i in range(1000000, 0, term) : 
    t = threading.Thread(target=jobs(i,i+term))
    threads.append(t) 

a = ()
# print(threads)
for t in threads : 
    a = t.start() # 스레드 시작
    
print(max_dic)
# for t in threads : 
#     t.join()  # 스레드 종료까지 대기

print(time.time()-start_time)


        
