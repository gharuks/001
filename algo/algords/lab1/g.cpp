#include<iostream>
#include <bits/stdc++.h>
#include<string>
using namespace std;
int main(){
    string s;
    stack <int> st;
    while(cin>>s){
         if(s=="+" || s=="-" || s=="*"){
            int a, b;
            a=st.top();
            st.pop();
            b=st.top();
            st.pop();
            if (s=="+") st.push(a+b);
            if (s=="-") st.push(a-b);
            if(s=="*") st.push(a*b);
        }
        else{
            st.push(stoi);
        }
    }
    cout<<st.top();
    return 0;
}