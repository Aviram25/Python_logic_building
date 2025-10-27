num1 = int(input())
english_newspaper = set(map(int,input().split()))
num2 = int(input())
french_newspaper = set(map(int,input().split()))

# unique_numbers = (english_newspaper | french_newspaper) - (english_newspaper & french_newspaper)

unique_nums = english_newspaper.symmetric_difference(french_newspaper)

print(len(unique_nums))  
