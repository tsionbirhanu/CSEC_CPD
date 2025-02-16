def medium(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)

t = int(input())

# Process each test case
for i in range(t):
    a, b, c = map(int, input().split())
    med = medium(a, b, c)
    print(med)
