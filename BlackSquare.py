calories = list(map(int, input().split()))  
s = input()  
total_calories = sum(calories[int(ch) - 1] for ch in s)
print(total_calories)
