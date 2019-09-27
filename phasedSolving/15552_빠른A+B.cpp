//15552 빠른A+B
#include <iostream>
using namespace std;

int main(){
    cin.tie(NULL);
    int c;
    cin>>c;
    int answer[c];
    for(int i=0;i<c;i++){
        int a,b;
        cin>>a>>b;
        answer[i]=a+b;
    }
    
    for(int i=0;i<c;i++){
        cout<<answer[i]<<"\n";
    }
}
