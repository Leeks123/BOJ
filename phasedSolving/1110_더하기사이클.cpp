//1110 더하기 사이클
#include <iostream>
using namespace std;

int cycle(int c,int cnt,int o){
    int a = c/10;
    int b = c%10;
    int n = b*10+(a+b)%10;
    cnt++;
    if(n==o){
        return cnt;
    }else{
        return cycle(n,cnt,o);
    }
}
int main(){
    cin.tie(NULL);
    int c;
    cin>>c;
    cout<<cycle(c,0,c)<<"\n";
}
