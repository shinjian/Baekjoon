# 쿠폰 - https://www.acmicpc.net/problem/10179
test = int(input())
for i in range(test):
    money = float(input())
    print("${:.2f}".format(round(money * 0.8, 2)))