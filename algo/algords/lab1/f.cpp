#include<iostream>
#include<stack>
using namespace std;
int main(){
    string s;
    stack <char> st;
    cin>>s;
    for(int i=0;i<s.size();i++){
        if(s[i]=='(' || s[i]=='{' || s[i]=='[') st.push(s[i]);
        else{
            if(s[i]!=')' && st.top()=='('){
                cout<<"no";
                return 0;
            }
            if(s[i]!='}' && st.top()=='{'){
                cout<<"no";
                return 0;
            }
            if(s[i]!=']' && st.top()=='['){
                cout<<"no";
                return 0;
            }
            st.pop();
        }
    }
    if(st.empty()) cout<<"yes";
    else cout<<"no";
    return 0;
}