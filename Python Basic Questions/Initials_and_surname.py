s = input("Enter the name --->  ")

n = s.split()
name_surname = ""
for i in range(len(n)):
    if n[i] == n[-1]:
        name_surname += n[-1]
    else:
        name_surname += n[i][0] + "."

print(name_surname)            
