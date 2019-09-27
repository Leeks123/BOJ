//10951 A+B 4
#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main(){
    vector<int> v;
    int a,b;
    while(scanf("%d %d",&a,&b)!=EOF){
        v.push_back(a+b);
    }
    vector<int>::iterator it;
    for(it=v.begin();it!=v.end();it++){
        cout<<*it<<"\n";
    }
}
