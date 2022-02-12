# 체스판 조각 - https://www.acmicpc.net/problem/3004
number = int(input())
if number % 2 == 0:
    print(((number//2) + 1) ** 2)
else:
    print(((number//2) + 1) * ((number//2) + 2))