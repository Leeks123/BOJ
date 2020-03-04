#include <iostream>
#include <vector>

using namespace std;
double proposition(vector<int> v){
    double sum=0,avg,cnt=0;
    for(int i=0;i<v.size();i++){
        sum+=v[i];
    }
    avg = sum/v.size();
    
    for(int i=0;i<v.size();i++){
        if(v[i]>avg) cnt++;
    }
    return cnt/v.size()*100;
}
int main(void){
    int c, n;
    cin>>c;
    vector<double> answer;
    for(int i=0;i<c;i++){
        cin>>n;
        vector<int> v;
        for(int i=0;i<n;i++){
            int score;
            cin>>score;
            v.push_back(score);
        }
        answer.push_back(proposition(v));
    }
    
    for(int i=0;i<answer.size();i++){
        cout<<fixed;
        cout.precision(3);
        cout<<answer[i]<<'%'<<endl;
    }
    return 0;
}
