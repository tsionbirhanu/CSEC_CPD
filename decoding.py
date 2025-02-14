def decode_word(n, s):
    original = []
    for i in range(n-1, -1, -1): 
        original.insert(len(original) // 2, s[i])  
    return "".join(original)

n = int(input())
s = input()
print(decode_word(n, s))
