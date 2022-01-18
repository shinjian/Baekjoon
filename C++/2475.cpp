// 검증수 - https://www.acmicpc.net/problem/2475
#include<stdio.h>

int main(){
    int num, result = 0;
    for(int i = 0; i <= 4; i++){
        scanf("%d", &num);
        result += num * num;
    }
    printf("%d", result % 10);
}