# list []
subway = [10,20,30]
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)

# 조세호가 타고있는 칸
print(subway.index("조세호"))

# 추가
subway.append("하하")
subway.insert(1,"정형돈")
print(subway)

# 삭제
print(subway.pop())
print(subway)
subway.clear();
print(subway)

# 정렬
num_list = [5,2,3,1,4]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)

#확장
mix_list = ["조세호",10, True]
num_list.extend(mix_list)
print(num_list) # [5, 4, 3, 2, 1, '조세호', 10, True]