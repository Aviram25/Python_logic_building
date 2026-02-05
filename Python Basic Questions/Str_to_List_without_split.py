s = "congrats you got placed"
index_of = 0
temp = []
for i in range(len(s)):
    if s[i] == " ":
        temp.append(s[index_of:i])
        index_of = i+1
temp.append(s[index_of:])        
print(temp)        