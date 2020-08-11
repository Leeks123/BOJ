// 2232 분해합

#include <iostream>
#include <cmath>

using namespace std;

int decomposition(int n){
    int ret=0;
    int cnt=0;
    while(n!=0){
        int term=n%10;
        n = n/10;
        ret += (1+pow(10,cnt++))*term;
    }
    return ret;
}

int main(){
    int n;
    cin>>n;
    
    int digit=0,tmp=n;
    while(tmp!=0){
        tmp = tmp/10;
        digit++;
    }
    
    for(int i=n-digit*10;i<n;i++){
        if(decomposition(i)==n) {
            cout<<i<<endl;
            break;
        }
    }
    return 0;
}
