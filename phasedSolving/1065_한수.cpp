//1065 한수
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> numPosition(int n){
    vector<int> v;
    while(n!=0){
        v.push_back(n%10);
        n=n/10;
    }
    reverse(v.begin(),v.end());
    return v;
}
bool isHan(int n){
    vector<int> v =numPosition(n);
    if((v[1]-v[0])==(v[2]-v[1])){
      return true;
    }else{
      return false;
    }
}
int main(){
    cin.tie(NULL);
    int n;
    cin>>n;
    int cnt=0;
    if(n>99) cnt=99;
    else cnt=n;
    for(int i=100;i<=n;i++){
        if(isHan(i)) cnt++;
    }
    cout<<cnt<<'\n';
}
