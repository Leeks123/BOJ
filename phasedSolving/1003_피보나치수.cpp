// 1003 피보나치 수

#include <iostream>
#include <utility>
#include <vector>

using namespace std;

const int MAX = 41;
vector<pair<int,int>> dp;

void fill(){
    dp.push_back(make_pair(0, 1));
    dp.push_back(make_pair(1, 0));
    for(int i=2;i<MAX;i++){
        pair<int,int> p = make_pair(
                            dp[i-1].first+dp[i-2].first,
                            dp[i-1].second+dp[i-2].second
                                    );
        dp.push_back(p);
    }
}
void answer(int n){
    cout<< dp[n].second<<" "<<dp[n].first<<endl;
}

int main(){
    int t;
    cin>>t;
    fill();
    vector<int> testcase;
    for(int i=0;i<t;i++){
        int n;
        cin>>n;
        testcase.push_back(n);
    }
    
    for(int i=0;i<t;i++){
        answer(testcase[i]);
    }
}
