# list : []
subway = [10,20,30]
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)

# 조세호가 타고있는 칸
print(subway.index("조세호"))

# 추가
subway.append("하하")
subway.insert(1,"정형돈")

# 삭제
print(subway.pop())
subway.clear()

# 정렬
num_list = [5,2,3,1,4]
num_list.sort()
num_list.reverse()

#확장
mix_list = ["조세호",10, True]
num_list.extend(mix_list)
print(num_list) # [5, 4, 3, 2, 1, '조세호', 10, True]