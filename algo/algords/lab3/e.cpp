#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main(){
	int n, max=-1000, res;
    cin>>n;
    vector<int> a(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    sort(a.begin(), a.end());
    for(int i=0;i<n;i++){
        if(a[i]>max){
            res=max;
            max=a[i];
        }
    }
    cout<<res<<"\n";
	return 0;
}