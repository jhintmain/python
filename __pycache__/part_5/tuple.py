# list () 보다 빠름 , 변경되지 않을값을 처리할때 최초선언된 변수로 고정.
menu = ("돈까스", "치즈까스")   
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 에러

name = "김종국"
age= 20
hobby = "코딩"
print(name,age, hobby)

(name,age, hobby) = ("김종국",20, "코딩")
print(name,age, hobby)