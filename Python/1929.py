# 소수 구하기 - https://www.acmicpc.net/problem/1929
import math
import sys
input = sys.stdin.readline

def Prime(num):
    if num < 2:
        return False
    
    square_root  = int(math.sqrt(num))
    for i in range(2, square_root+1):
        if num % i == 0:
            return False
    return True

m, n = map(int, input().split())
for i in range(m, n+1):
    if Prime(i):
        print(i)