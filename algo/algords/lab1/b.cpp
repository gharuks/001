#include<iostream>
using  namespace std;
#define null 1e9
int st=0, en=0;
int q[100000];
bool empty(){
    return en-st<=0;
}void push(){
    int m;
    cin>>m;
    q[en]=m;
    en++;
    cout<<"ok\n";
}void pop(){
    if(empty()) cout<<"error\n";
    else{
        cout<<q[st]<<endl;
        q[st]=null;
        st++;
    }
}void front(){
    if(empty()) cout<<"error\n";
    else cout<<q[st]<<endl;
}void back(){
    if(empty()) cout<<"error\n";
    else cout<<q[en]<<endl;
}void size(){
    cout<<en-st<<endl;
}void clear(){
    for(int i=st;i<en;i++)
        q[i]=null;
    st=0;
    en=0;
    cout<<"ok\n"; 
}int main(){
    string t;
    while(true){
        cin>>t;
        if(t=="exit"){
            cout<<"bye";
            return 0;
        }
        if(t=="push") push();
        if(t=="size") size();
        if(t=="pop") pop();
        if(t=="back") back();
        if(t=="clear") clear();
        if(t=="front") front();
    }   
}
