# def getMyDivisor(n):

#     divisorsList = []

#     for i in range(1, int(n**(1/2)) + 1):
#         if (n % i == 0):
#             divisorsList.append(i) 
#             if ( (i**2) != n) : 
#                 divisorsList.append(n // i)

#     # divisorsList.sort()
    
#     return divisorsList

# # num = 1
# # while True : 
# #     samgaksu = sum([x for x in range(1,num+1)])
# #     divisor = getMyDivisor(samgaksu)
# #     if len(divisor) >= 500 :
# #         print(samgaksu)
# #         break
# #     else : 
# #         num += 1
    
# #     if num > 500000 :break

# print(getMyDivisor(76576500))
# print(len(getMyDivisor(76576500)))

def f(n):                                 # 약수 개수 구하는 함수
    count = 2
    if n**0.5 == int(n**0.5):             # n이 제곱수일 경우
        for i in range(2,int(n**0.5)):
            if n%i == 0:
                count += 2
        count += 1
    if not n**0.5 == int(n**0.5):         # n이 제곱수가 아닐 경우
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                count += 2  
    return count

''' i*(i+1)/2의 약수 개수는 i가 짝수일 경우 i/2와 i-1의 약수 개수의 곱과 같음을 이용 '''
for i in range(1,99999):
    if i%2 == 0:
        if f(int(i/2))*f(i+1) >= 500:
            print(i,i*(i+1)/2)
            break
    if i%2:
        if f(int(i))*f(int((i+1)/2)) >= 500:
            print(i,i*(i+1)/2)
            break

