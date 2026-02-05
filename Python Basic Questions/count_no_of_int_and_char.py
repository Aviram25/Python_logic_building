s = "Aviram123456789gmailcom"
count_char = 0
count_int = 0
for i in s:
    if i.isalpha():
        count_char+=1
    else:
        count_int+=1
print(count_char)
print(count_int)        