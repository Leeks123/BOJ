// 2309 일곱난쟁이

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

void printAnswer(int i,int j,vector<int> v){
    for(int n=0;n<v.size();n++){
        if( n==i || n==j ) continue;
        cout<<v[n]<<endl;
    }
}

int main(){
    vector<int> littles;
    int total=0;
    for(int i=0;i<9;i++){
        int n;
        cin>>n;
        littles.push_back(n);
        total+=n;
    }
    sort(littles.begin(),littles.end());
        
    int tmp = total;
    for(int i=0;i<9;i++){
        tmp-=littles[i];
        for(int j=0;j<9;j++){
            if(i==j) continue;
            if(tmp-littles[j]==100){
                printAnswer(i,j,littles);
                return 0;
            }
        }
        tmp = total;
    }
    
    
    return 0;
}
