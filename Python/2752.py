# 세수정렬 - https://www.acmicpc.net/problem/2752
number = list(map(int, input().split()))
number = sorted(number)
for i in range(3):
    print(number[i], end=" ")