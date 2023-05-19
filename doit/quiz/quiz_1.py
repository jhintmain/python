# a:b:c:d -> a#b#c#d로 바꾸니

word= "a:b:c:d"
change_word = word.replace(":","#")

print(change_word)