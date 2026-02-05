s = "hello hello hello bhai bhai bhai chi chi chi"

n = s.split()
temp = []
for i in n:
    if i not in temp:
        temp.append(i)
print(" ".join(temp))        