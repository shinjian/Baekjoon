# 별 찍기 - 5 - https://www.acmicpc.net/problem/2442
n = int(input())
for i in range(1, n+1):
    print(' '*(n-i) + '*'*(i*2-1))