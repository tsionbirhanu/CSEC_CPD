s1, s2, s3, s4 = map(int, input().split())
distinct_colors = len(set([s1, s2, s3, s4]))
horseshoes_to_buy = 4 - distinct_colors

print(horseshoes_to_buy)
