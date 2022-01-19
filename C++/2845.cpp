#include<iostream>
using namespace std;

int main(){
    int l, p, a[5];
    cin >> l >> p;
    cin >> a[0] >> a[1] >> a[2] >> a[3] >> a[4];
    int b = l*p;
    for(int i=0; i<5; i++){
        cout << a[i] - b << ' ';
    }
}