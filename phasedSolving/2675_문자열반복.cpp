
#include <iostream>
#include <string>
using namespace std;

string solve(int n,string str){
    string ret = "";
    for(int i=0;i<str.length();i++){
        for(int j=0;j<n;j++){
            ret+=str[i];
        }
    }
    return ret;
}
int main(int argc, const char * argv[]) {
    int t;
    cin>>t;
    string str;
    string answer[t];
    int n;
    for(int i=0;i<t;i++){
        cin>>n>>str;
        answer[i]=solve(n,str);
    }
    for(int i=0;i<t;i++){
        cout<<answer[i]<<'\n';
    }
    return 0;
}
