#include<iostream>
using  namespace std;
#define null 1e9
int st=50000, en=50000;
int d[100000];
bool empty(){
    return en-st<=0;
}void push_front(){
    int m;
    cin>>m;
    d[st]=m;
    st--;
    cout<<"ok\n";
}void push_back(){
    int m;
    cin>>m;
    d[en+1]=m;
    en++;
    cout<<"ok\n";
}
void pop_front(){
    if(empty()) cout<<"error\n";
    else{
        cout<<d[st+1]<<endl;
        st++;
    }
}void pop_back(){
    if(empty()) cout<<"error\n";
    else{
        cout<<d[en]<<endl;
        en--;
    }
}
void front(){
    if(empty()) cout<<"error\n";
    else cout<<d[st+1]<<endl;
}void back(){
    if(empty()) cout<<"error\n";
    else cout<<d[en]<<endl;
}void size(){
    cout<<en-st<<endl;
}void clear(){
    for(int i=st;i<en;i++)
        d[i]=null;
    st=50000;
    en=50000;
    cout<<"ok\n"; 
}int main(){
    string s;
    while(cin>>s){
        if(s=="exit"){
            cout<<"bye\n";
            return 0;
        }
        if(s=="push_front") push_front();
        if(s=="push_back") push_back();
        if(s=="pop_front") pop_front();
        if(s=="pop_back") pop_back();
        if(s=="front") front();
        if(s=="back") back();
        if(s=="size") size();
        if(s=="clear") clear();
    }
}
