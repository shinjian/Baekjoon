#include<iostream>
using namespace std;

int main(){
    int answer[6];
    int list[6] = {1,1,2,2,2,8};
    for(int i=0; i<6; i++){
        cin >> answer[i];
    }
    for(int j=0; j<6; j++){
        cout << list[j] - answer[j] << ' ';
    }
}