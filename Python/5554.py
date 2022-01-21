# 심부름 가는 길 - https://www.acmicpc.net/problem/5554
distance = 0
for _ in range(4):
    distance += int(input())
print(distance // 60)
print(distance % 60)