// 2748 피보나치수2

#include <iostream>
#include <vector>

using namespace std;

const int MAX = 91;
long fibonacci[MAX];

void fill(){
    fibonacci[0]=0;
    fibonacci[1]=1;
    for(int i=2;i<MAX;i++){
        fibonacci[i]=fibonacci[i-1]+fibonacci[i-2];
    }
}
int main(){
    int n;
    cin>>n;
    fill();
    
    cout<<fibonacci[n];

//    for(int i=0;i<MAX;i++){
//        cout<<fibonacci[i]<<endl;
//    }
}
