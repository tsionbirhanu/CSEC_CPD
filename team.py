problems = int(input())
solved = 0 

for _ in range(problems):
    petya, vasya, tonya = map(int, input().split())
    if petya + vasya + tonya >= 2:
        solved += 1

print(solved)
