k, r = map(int, input().split())  
n = 1 

while True:
    total = n * k 
    if total % 10 == r or total % 10 == 0:
        break
    n += 1  

print(n)
