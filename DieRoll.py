import math
Y, W = map(int, input().split())
M = max(Y, W)
numerator = 7 - M
denominator = 6
gcd_value = math.gcd(numerator, denominator)
print(f"{numerator // gcd_value}/{denominator // gcd_value}")
