//17300 패턴
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

bool isDuplicated(vector<int> v){
    vector<int> check(10);
    for(int i=0;i<v.size();i++){
        check[v[i]]++;
    }
    for(int i=0;i<check.size();i++){
        if(check[i]>1) return true;
    }
    return false;
}
bool ableToGo(int src, int dest){
    switch (src) {
        case 1:
            if(dest==2 || dest==4 || dest==5 || dest==8 || dest==6) return true;
            else return false;
        case 2:
            if(dest==1 || dest==3 || dest==4 || dest==5 || dest==6 || dest==7 || dest==9) return true;
            else return false;
        case 3:
            if(dest==2 || dest==5 || dest==6 || dest==4 || dest==8) return true;
            else return false;
        case 4:
            if(dest==1 || dest==2 || dest==5 || dest==7 || dest==8 || dest==3 || dest==9) return true;
            else return false;
        case 5:
            if(dest==1 || dest==2 || dest==3 || dest==4 || dest==6
               || dest==7 || dest==8 || dest==9 ) return true;
            else return false;
        case 6:
            if(dest==2 || dest==3 || dest==5 || dest==8 || dest==9 || dest==1 || dest==7) return true;
            else return false;
        case 7:
            if(dest==4 || dest==5 || dest==8 || dest==2 || dest==6) return true;
            else return false;
        case 8:
            if(dest==4 || dest==5 || dest==6 || dest==7 || dest==9 || dest==1 || dest==3) return true;
            else return false;
        case 9:
            if(dest==5 || dest==6 || dest==8 || dest==2 || dest==4) return true;
            else return false;

        default:
            break;
    }
    return false;
}
bool isContinuous(vector<int> v){
    
    for(int i=0;i<v.size()-1;i++){
        if(ableToGo(v[i], v[i+1])){
            continue;
        } else {
            if(abs(v[i]-v[i+1])==1*2){
                if(v[i]<v[i+1]){
                    if(find(v.begin(),v.begin()+i+2,v[i]+1)!=(v.begin()+i+2)){
                        continue;
                    }else{
                        return false;
                    }
                }else{
                    if(find(v.begin(),v.begin()+i+2,v[i]-1)!=(v.begin()+i+2)){
                        continue;
                    }else{
                        return false;
                    }
                }
            }else if(abs(v[i]-v[i+1])==2*2){
                if(v[i]<v[i+1]){
                    if(find(v.begin(),v.begin()+i+2,v[i]+2)!=(v.begin()+i+2)){
                        continue;
                    }else{
                        return false;
                    }
                }else{
                    if(find(v.begin(),v.begin()+i+2,v[i]-2)!=(v.begin()+i+2)){
                        continue;
                    }else{
                        return false;
                    }
                }
            }else if(abs(v[i]-v[i+1])==3*2){
                if(v[i]<v[i+1]){
                    if(find(v.begin(),v.begin()+i+2,v[i]+3)!=(v.begin()+i+2)){
                        continue;
                    }else{
                        return false;
                    }
                }else{
                    if(find(v.begin(),v.begin()+i+2,v[i]-3)!=(v.begin()+i+2)){
                        continue;
                    }else{
                        return false;
                    }
                }
            }else if(abs(v[i]-v[i+1])==4*2){
                if(v[i]<v[i+1]){
                    if(find(v.begin(),v.begin()+i+2,v[i]+4)!=(v.begin()+i+2)){
                        continue;
                    }else{
                        return false;
                    }
                }else{
                    if(find(v.begin(),v.begin()+i+2,v[i]-4)!=(v.begin()+i+2)){
                        continue;
                    }else{
                        return false;
                    }
                }
            } else {
                return false;
            }
        }
    }
    
    return true;
}
bool isValid(vector<int> v){
    if(v.size()<3) return false; // 패턴 사이즈 검증
    if(isDuplicated(v)) return false; // 중복 값 체크
    if(!isContinuous(v)) return false; // 패턴의 연속성 체크
    return true;
}
int main(){
    int n;
    cin>>n;
    vector<int> pattern;
    for(int i=0;i<n;i++){
        int input;
        cin>>input;
        pattern.push_back(input);
    }
    if(isValid(pattern)){
        cout<<"YES"<<endl;
    }else{
        cout<<"NO"<<endl;
    }
}
