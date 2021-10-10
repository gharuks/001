#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main(){
	int n, max=-1000;
    cin>>n;
    vector<int> a(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    for(int i=0;i<n;i++){
        if(a[i]>=max) max=a[i];
    }
    cout<<max<<"\n";
	return 0;
}