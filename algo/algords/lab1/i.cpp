#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    deque <int> first, second;
    for(int i=0;i<n;i++){
        char ch;
        cin>>ch;
        if(ch=='+'){
            int i;
            cin>>i;
            first.push_back(i);
            if(first.size()>second.size()){
                second.push_back(first.front());
                first.pop_front();
            }
        } 
        else if(ch=='*'){
            int i;
            cin>>i;
            first.push_front(i);
            if(first.size()>second.size()){
                second.push_back(first.front());
                first.pop_front();
            }
        } 
        else{
            cout<<second.front()<<"\n";
            second.pop_front();
            if(first.size()>second.size()){
                second.push_back(first.front());
                first.pop_front();
            }
        }
    }
    return 0;
}