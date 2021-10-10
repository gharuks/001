#include <iostream>
#include <bits/stdc++.h>
using namespace std;
const int N=(int)1e5+5;
int a[N], n, m;
bool bin_search(int x){
	if(x<a[1] || a[n]<x)
		return false;
	int l=1, r=n;
	while(l<=r){
		int mid=(l+r)/2;
		if(a[mid]==x)
			return true;
		if(a[mid]<x) l=mid+1;
		else r=mid-1;
	}
	return false;
}
int main(){
    cin>>n>>m;
    for(int i=1;i<=n;i++){
        cin>>a[i];
    }
    sort(a+1, a+n+1);
    for(int i=1;i<=m;i++){
        int b;
        cin>>b;
        if(bin_search(b)) cout<<"YES\n";
        else cout<<"NO\n";
    }
	return 0;
}