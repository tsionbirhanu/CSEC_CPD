def process_shots(n, birds, m, shots):
    for xi, yi in shots:
        xi -= 1
        yi -= 1
        if xi > 0:
            birds[xi - 1] += yi
        if xi < n - 1:
            birds[xi + 1] += birds[xi] - (yi + 1)
        birds[xi] = 0
    return birds

n = int(input())
birds = list(map(int, input().split()))
m = int(input())
shots = [tuple(map(int, input().split())) for _ in range(m)]

final_birds = process_shots(n, birds, m, shots)

for count in final_birds:
    print(count)
