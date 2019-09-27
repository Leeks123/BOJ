
#include <iostream>
using namespace std;
bool bigger(int a,int b){
    int tmp = a>b ? a : b;
    if(tmp==a) return true;
    else return false;
}
bool ascending(int* arr){
    for(int i=0;i<7;i++){
        if(bigger(arr[i],arr[i+1])){
            return false;
        }
    }
    return true;
}
bool descending(int* arr){
    for(int i=0;i<7;i++){
        if(bigger(arr[i+1],arr[i])){
            return false;
        }
    }
    return true;
}
int main(){
    int arr[8];
    for(int i=0;i<8;i++){
        cin>>arr[i];
    }
    
    if(ascending(arr)){
        cout<<"ascending"<<endl;
    }else if(descending(arr)){
        cout<<"descending"<<endl;
    }else{
        cout<<"mixed"<<endl;
    }
}
