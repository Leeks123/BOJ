
#include <iostream>
#include <string>
#include <algorithm>
#include <map>
using namespace std;

int main(int argc, const char * argv[]) {
    string str;
    cin>>str;
    transform(str.begin(),str.end(),str.begin(),::toupper);
    
    map<char,int> m;
    for(int i=0;i<str.length();i++){
        if(m.find(str[i])==m.end()){
            m.insert(make_pair(str[i],1));
        }else{
            m[str[i]]+=1;
        }
    }
    pair<char,int> answer=make_pair('a',0);
    map<char,int>::iterator it;
    for(it=m.begin();it!=m.end();it++){
        if(it->second > answer.second){
            answer.first = it->first;
            answer.second = it->second;
        }else if(it->second == answer.second){
            answer.first='?';
        }
    }
    cout<<answer.first<<'\n';
    return 0;
}
