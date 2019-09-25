//10818
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    vector<int> v;
    int n;
    cin>>n;
    int s;
    for(int i=0;i<n;i++){
        cin>>s;
        v.push_back(s);
    }
    sort(v.begin(),v.end());
    cout<<*(v.begin())<<' '<<*(v.end()-1)<<endl;
}

