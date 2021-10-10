#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n, m;
    vector <int> a(n);
    cin>>n>>m;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    while(m--){
        int x; cin>>x;
        int l=-1, r=n;
        while(r-l>1){
            int mid=(l+r)/2;
            if(a[mid]<x) l=mid;
            else r=mid;
        }
        int l1=-1, r1=n;
        while(r1-l1>1){
            int mid=(l1+r1)/2;
            if(a[mid]<=x) l1=mid;
            else r1=mid;
        }
        if(l1>=r) cout<<r+1<<" "<<l1+1<<'\n';
        else cout<<0<<'\n';
    }
	return 0;
}