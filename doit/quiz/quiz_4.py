# A = [20,55,67,82,45,33,90,87,100,25] 에서 50점이상 점수의 총합

A = [20,55,67,82,45,33,90,87,100,25]

filter_A = [score for score in A if score >= 50]

sum_A = sum(filter_A)

print(sum_A)