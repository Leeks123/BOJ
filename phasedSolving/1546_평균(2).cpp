
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<double> changeScore(int m,vector<int> v){
    vector<double> ret;
    for(int i=0;i<v.size();i++){
        ret.push_back((double)v[i]/m*100);
    }
    return ret;
}
int main(void){
    int n;
    cin>>n;
    vector<int> v;
    for(int i=0;i<n;i++){
        int in;
        cin>>in;
        v.push_back(in);
    }
    
    sort(v.begin(),v.end());
    int m = v[v.size()-1];
    vector<double> cv = changeScore(m, v);
    double sum=0;
    for(int i=0;i<n;i++){
        sum+=cv[i];
    }
    cout<<sum/n<<endl;
    return 0;
}
