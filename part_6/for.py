# for list in [1,2,3,4,5] :
#     print("대기번호 : {0}".format(list))

# for list in range(1,6) :
#     print("대기번호 : {0}".format(list))

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{} , 커피가 준비되었습니다 {}번 남앗어요".format(customer, index))
#     index -=1
#     if index == 0:
#         print("커피버림")

# customer = "토르"
# person = "Unknown"
# while person !=customer:
#     print("{} , 커피가 준비되었습니다".format(customer))
#     person = input("이름이 어떻게 되세요?")
    

absent = [2,5]
nobook = [7]
student = range(1,11)

for student in range(1,11):
    if student in absent :
        continue
    elif student in nobook:
        print("{}번 끝나고 교무실로 따라와".format(student))
        break
    else:
        print("{}번 책을 읽는다".format(student))



# students = [1,2,3,4,5]
# students = [i+100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)