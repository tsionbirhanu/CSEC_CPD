n = int(input())
prev = input()
groups = 1

for _ in range(n - 1):
    curr = input()
    if curr != prev:
        groups += 1
    prev = curr

print(groups)
