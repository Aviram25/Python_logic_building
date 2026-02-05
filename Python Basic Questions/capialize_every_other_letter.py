s = "i got placed"
c = ""
for i in range(len(s)):
    if i%2==0:
        c += s[i].upper()
    else:
        c += s[i].lower()
print(c)            