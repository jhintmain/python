
# for week in range(1,51) :
#     with open(str(week)+"주차.txt","w", encoding="utf8") as study_file:
#         study_file.write("- {}주차 주간 보고 -\n".format(week))
#         study_file.write("부서 : \n")
#         study_file.write("이름 : \n")
#         study_file.write("업무 요약 :")

for week in range(1,11) : 
    with open(str(week)+"주차.txt", "w", encoding="utf8") as report:
        report.write("- {} 주차 주간보고 -\n".format(week))
        report.write("부서 : \n")
        report.write("이름 : \n")
        report.write("업무요약 : \n")