# 가위 바위 보? - https://www.acmicpc.net/problem/4493
T = int(input())
for _ in range(T):
    n = int(input())
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        p1, p2 = map(str, input().split())
        res = ord(p1) - ord(p2)
        if res == -2 or res == -1 or res == 3:
            cnt1 += 1
        elif res == 2 or res == 1 or res == -3:
            cnt2 += 1
    if cnt1 > cnt2:
        print("Player 1")
    elif cnt1 < cnt2:
        print("Player 2")
    else:
        print("TIE")