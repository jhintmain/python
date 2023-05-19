# input_str = input("입력 : ")
# input_arr = input_str.split(" ")

# for num in input_arr :
#     num = set(num)
    
#     if len(num) == 10 : 
#         print("True",end = " ")
#     else :
#         print("False", end=" ")
    
################################################
input_str = input("입력 : ")

before_n_odd_even = 0 
for i, n in enumerate(input_str) :

    n = int(n)
    if i != 0 : 
        n_odd_even = "even" if n%2 == 0 else "odd"

        if before_n_odd_even == n_odd_even :        
            if n_odd_even == "even" :
                print("*",end="") 
            else : 
                print("-",end="")
    print(n,end="") 
    before_n_odd_even = "even" if n%2 == 0 else "odd"