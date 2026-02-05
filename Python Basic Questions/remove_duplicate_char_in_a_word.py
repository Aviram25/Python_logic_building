s = "aviram"
a = s.split()
e = []
for i in s:
    if i not in e:
        e.append(i)
print("".join(e))         