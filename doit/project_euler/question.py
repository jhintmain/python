# Q1. 1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?

# total = 0
# for i in range(1,1000) :
#     if i%3 == 0 or i%5 == 0 : 
#         total += i

# print(total)

# Q2. 4백만 이하의 짝수 값을 갖는 모든 피보나치 항을 더하면 얼마가 됩니까?
# start_num = 1
# end_num = 2
# total = 2
# while True : 
#     next_num = start_num + end_num

#     if next_num > 4000000 : 
#         break
    
#     if next_num % 2 == 0 : 
#         total += next_num

#     start_num,end_num = end_num,next_num

# print(total)
    
    
# Q3. 600851475143 의 소인수 중에서 가장 큰 수를 구하세요.

# x = 600851475143
# min = 2
# while min <= x : 
#     if x % min == 0 : # 소인수임
#         # print(min)
#         x //= min
#     else : 
#          min +=1

# print(min)

# Q4. 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
# 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?
# print("========= Q4 =========")

# answer = 0
# for first in range(999,99,-1) : 
#     for last in range(999,99,-1) :

#         ori = str(first * last)
#         rvs = list(ori[:])
#         rvs.reverse()
#         rvs = ''.join(rvs)

#         if ori == rvs :
#             # print(ori,first,last)
#             if int(ori) > int(answer) : 
#                 answer = ori

# print(answer)

# Q5. 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수
print("========= Q5 =========")
# import math
# print(math.lcm(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
# stop_flag = False
# num = 20

# while True :    
#     for i in range(1,21) :
        
#         if num % i == 0 :
#             stop_flag = True        
#         else :
#             num += 20
#             stop_flag = False
#             break
#         if(i > 10) : 
#             print(num,i)
    
#     if stop_flag == True :
#        break

# # Q6. 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이
# print("========= Q6 =========")

# hap_pow = sum(list(range(1,101))) ** 2
# pow_hap = sum(list(map(lambda x : x**2,list(range(1,101)))))

# print(hap_pow)
# print(pow_hap)
# print(hap_pow - pow_hap)

# # Q7. 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다. 이 때 10,001번째의 소수를 구하세요
# print("========= Q7 =========")
# from primePy import primes
import time
# start_time = time.time()
# print(primes.first(10001)[10000])
# print(f"{time.time()-start_time:.4f}")


# Q8. 1000자리 수에서 연속한 13개 숫자의 곱이 가장 큰 값은 얼마입니까?
# print("========= Q8 =========")
# word = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
# piece_size = 13
# max = 0

# def mul_list(args):
#     total = 1
#     for i in args :
#         total *= int(i)
#     return total

# for i in range(len(word)-piece_size+1) : 
#     a = list(word[i:i+piece_size])

#     if '0' not in a : 
#         # print(a)
#         tmp = mul_list(a)
#         if max < tmp :
#             max = tmp

# print(max)   
    
# Q9. a2 + b2 = c2 를 만족하면 피타고라스 수라고 부릅니다  a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?
# print("========= Q9 =========")

# for a in range(1, 1000) :
#     for b in range(a,1000) :
#         c = 1000-a-b
#         if a**2 + b**2 == c**2 : 
#             # print(a,b,c)
#             print(a*b*c)
#             break

start_time = time.time()
num = 2000000
q10_list = dict([])

for i in range(2,num+1) : 
    q10_list[i] = 0

for i in range(2,num+1) : 
    if q10_list[i] == 0 :
        n = 2
        while i*n <= num : 
            q10_list[i*n] = 1
            n+=1

sum = 0

for i in range(2,num+1) : 
    if q10_list[i] == 0 :
        sum += i

print(sum)
print(time.time()-start_time)