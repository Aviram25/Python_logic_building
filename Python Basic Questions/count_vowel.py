c = "computer"

caps = ["A","E","I","O","U"]
small = ["a","e","i","o","u"]
count = 0
for i in c:
    if (i in caps) or (i in small):
        count+=1
print(count)        