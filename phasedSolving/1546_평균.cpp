
#include <iostream>
using namespace std;

double avg(int n,int* arr){
    double sum=0;
    for(int i=0;i<n;i++){
        sum+=arr[i];
    }
    return (double)(sum/n);
}
double fabrication(double n,double l){
    return n/(double)l*100;
}
int big(int n,int* arr){
    int ret = arr[0];
    for(int i=0;i<n;i++){
        if(ret<arr[i]){
            ret=arr[i];
        }
    }
    return ret;
}
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    int b = big(n,arr);
    for(int i=0;i<n;i++){
        arr[i]=fabrication(arr[i], b);
    }
    cout<<avg(n,arr)<<endl;
}
