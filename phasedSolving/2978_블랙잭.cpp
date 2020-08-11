// 2798 블랙잭

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int n,m;
    cin>>n>>m;
    vector<int> cards;
    for(int i=0;i<n;i++){
        int input;
        cin>>input;
        cards.push_back(input);
    }
    sort(cards.begin(),cards.end());
    
    int sum=0;
    for(int x=0;x<cards.size();x++){
        for(int y=0;y<cards.size();y++){
            if(x==y) continue;
            for(int z=0;z<cards.size();z++){
                if(z==x || z==y) continue;
                if(cards[x]+cards[y]+cards[z]<=m && cards[x]+cards[y]+cards[z]>sum){
                    sum = cards[x]+cards[y]+cards[z];
                }
            }
        }
    }
    cout<<sum;
    return 0;
}
