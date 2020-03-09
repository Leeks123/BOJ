#include <iostream>

using namespace std;

int sumRange(int n){
    int i=0;
    while(true){
        int sum=i*(i+1)/2,nextSum = (i+1)*(i+2)/2;
        if(n>sum && n<=nextSum){
            break;
        }
        i++;
    }
    return i+1;
}
int main(void){
    int n;
    cin>>n;
    // 1/1 - 1/2 2/1 - 3/1 2/2 1/3 - 1/4 2/3 3/2 4/1
    //  1     2   3     4   5   6     7   8   9   10
    int s = sumRange(n);
    int d = s*(s+1)/2-n;
    if(s%2==0){
        cout<<s-d<<"/"<<d+1<<endl;
    }else{
        cout<<d+1<<"/"<<s-d<<endl;
    }
    
    return 0;
}
