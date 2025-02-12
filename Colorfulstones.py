s = input().strip()
t = input().strip()
current_position = 0
for instruction in t:
    if s[current_position] == instruction:
        current_position += 1
        if current_position == len(s):
            break

print(current_position + 1)
