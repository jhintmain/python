def std_weight(height, gender) :
    const = 22
    height_m = height*0.01
    if gender == "여자" :
        const = 21

    return height, gender, round(height_m*height_m*const,2)


(height , gender, weight) = std_weight(160,"여자")
print("키 {}cm {}의 표준체중은 {}kg 입니다".format(height,gender,weight))    
