# def std_weight(height, gender) :
#     const = 22
#     height_m = height*0.01
#     if gender == "여자" :
#         const = 21

#     return height, gender, round(height_m*height_m*const,2)


# (height , gender, weight) = std_weight(160,"여자")
# print("키 {}cm {}의 표준체중은 {}kg 입니다".format(height,gender,weight))    




def std_weight(height,gender):
    
    height_m = height/100
    if gender == "여자":
        value = 22
    else :
        value = 21

    weight = height_m*height_m*value

    return height, gender, weight

(height , gender, weight) = std_weight(175,"남자")
print("키 {}cm {}의 표준체중은 {:.2f}kg 입니다".format(height,gender,weight))    
