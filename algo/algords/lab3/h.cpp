#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int l=1, r=n, cnt=0;
    while(l<r){
        l*=2;
        cnt++;
    }
    cout<<cnt<<"\n";
	return 0;
}