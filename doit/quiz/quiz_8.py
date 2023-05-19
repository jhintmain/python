import os

with open(os.path.dirname(__file__)+"/abc.txt", "w") as f :
    for i in range(ord('A'),ord('E')+1) :
        f.write(chr(i)*3+"\n")


f = open(os.path.dirname(__file__)+"/abc.txt", "r")
abc_list = f.readlines()
abc_reverse_list = abc_list[:]
abc_reverse_list.reverse()
f.close()

with open(os.path.dirname(__file__)+"/abc.txt", "w") as f :
    for line in abc_reverse_list :
        f.write(line)
    

