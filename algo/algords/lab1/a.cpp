#include<iostream>
using  namespace std;
#define null 1e9
int n=0;
long long m;
long long s[100000];
bool error(){
    return n-1<0;
}void push(){
    cin>>m;
    s[n]=m;
    n++;
    cout<<"ok\n";
}void pop(){
    if(error()) cout<<"error\n";
    else{
        cout<<s[n-1]<<endl;
        s[n-1]=null;
        n--;
    }
}void back(){
    if(error()) cout<<"error\n";
    else cout<<s[n-1]<<endl;
}void size(){
    cout<<n<<endl;
}void clear(){
    for(long long i=0;i<m;i++)
        s[i]=null;
    n=0;
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
    }   
    return 0;
}