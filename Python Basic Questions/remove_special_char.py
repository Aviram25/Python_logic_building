# s = "This$ is where* error Comes&"

# a = ""

# for i in s:
#     if i.isalpha():
#         a+=i
#     else:
#         a+=" "
# print(" ".join(a.split()))




def eee(s):
    s = s.split()
    temp = []
    for i in s:
        temp.append(i[::-1])

    print(*temp)

s = "hello how are you"
result = eee(s)
