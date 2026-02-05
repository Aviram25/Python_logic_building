s = "YESSSSSSSSSSSSSSS i got placed in multiple companies"

n = s.split()
smallest = float('inf')
largest = float('-inf')

lar = ""
sma = ""
for i in range(len(n)):
    if largest < len(n[i]):
        largest = len(n[i])
        lar= n[i]

    if len(n[i]) < smallest:
        smallest = len(n[i])
        sma = n[i]    
print(lar)
print(sma)        