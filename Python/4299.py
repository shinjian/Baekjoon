# AFC 윔블던 - https://www.acmicpc.net/problem/4299
sum, m = map(int, input().split())
if  (sum + m < 0 or sum - m < 0) or ((sum + m) % 2):
    print(-1)
else:
    result1 = (sum+m) // 2
    reuslt2 = sum - result1
    print(max(result1, reuslt2), min(result1, reuslt2))