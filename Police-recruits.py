n = int(input()) 
events = list(map(int, input().split())) 
police_officers = 0
untrted_crimes = 0
for event in events:
    if event == -1: 
        if police_officers > 0:
            police_officers -= 1  
        else:
            untrted_crimes += 1  
    else:
        police_officers += event 

print(untrted_crimes)
