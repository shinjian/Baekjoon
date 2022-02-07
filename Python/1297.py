# TV 크기 - https://www.acmicpc.net/problem/1297
d, high, width = map(int, input().split())
a = d  / ((high ** 2 + width ** 2) ** 0.5)
print(int(high * a), int(width * a))