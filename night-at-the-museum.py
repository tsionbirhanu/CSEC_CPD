s = input().strip()
current_position = 'a'
total_rotations = 0
for char in s:
    clockwise_distance = abs(ord(char) - ord(current_position))
    counterclockwise_distance = 26 - clockwise_distance
    total_rotations += min(clockwise_distance, counterclockwise_distance)
    current_position = char
print(total_rotations)

