#include<iostream>
#include<bits/stdc++.h>
using namespace std;
struct Node{
    int val;
    Node* left;
    Node* right;
    Node(int x){
        val=x;
        left=right=NULL;
    }
};
struct BST{
    Node* root=NULL;
    void add(Node* node, int x){
        if(node->val==x) return;
        if(node->val>x){
            if(node->left==NULL){
                node->left=new Node(x);
                return;
            }
            add(node->left, x);
            return;
        }
        if(node->right==NULL){
            node->right=new Node(x);
            return;
        }
        add(node->right, x);
    }
    void add(int x){
        if(root==NULL){
            root=new Node(x);
            return;
        }
        add(root, x);
    }
    int height(){
        return height(root);
    }
    int height(Node* node){
        if(node==NULL) return 0;
        int l=height(node->left);
        int r=height(node->right);
        return max(l, r); // return max(l,r);
    }
    bool balanced(){
        balanced(root);
    }
    bool balanced(Node* node){
        int l=height(node->left), r=height(node->right);
        if(node==NULL) return true;
        if(abs(l-r)<=1) return true;
        return false;
    }
    int count(){
        return count(root);
    }
    int count(Node* node){
        if(node==NULL) return 0;
        int l=count(node->left);
        int r=count(node->right);
        return l+r+1;
    }
    void print(){
        print(root);
    }
    void print(Node* node){
        if(node==NULL) return;
        print(node->left);
        cout<<node->val<<"\n";
        print(node->right);
    }
    int maxval(){
        return maxval(root);
    }
    int maxval(Node* node) {
        while(node->right!=NULL){
            node=node->right;
        }
        return node->val;
    }
    int secmaxval(){
        return secmaxval(root, maxval(root));
    }
    int secmaxval(Node* node, int maxval){
        int cur;
        if(node==NULL) return 0;
        while (node!=NULL){
            if(node->val<maxval){
                cur=node->val;
                node=node->right;
            }
            else node=node->left;
        }
        return cur;
    }
    void leaves(){
        leaves(root);
    }
    void leaves(Node* node){
        if(node==NULL) return;
        leaves(node->left);
        if(node->left==NULL && node->right==NULL) cout<<node->val<<"\n";
        leaves(node->right);
    }
    void twochildren(){
        twochildren(root);
    }
    void twochildren(Node* node){
        if(node==NULL) return;
        twochildren(node->left);
        if(node->left!=NULL && node->right!=NULL) cout<<node->val<<"\n";
        twochildren(node->right);
    }
    void onechild(){
        onechild(root);
    }
    void onechild(Node* node){
        if(node==NULL) return;
        onechild(node->left);
        if(node->right!=NULL && node->left==NULL || node->right==NULL && node->left!=NULL) cout<<node->val<<"\n";
        onechild(node->right);
    }
};
int main(){
    int n;
    cin>>n;
    BST bst;
    while(n!=0){
        bst.add(n);
        cin>>n;
    }
    // cout<<bst.height()<<"\n";
    // cout<<bst.count()<<"\n";
    // cout<<bst.secmaxval()<<"\n";
    // bst.print();
    // bst.leaves();
    // bst.twochildren();
    // bst.onechild();
    if(bst.balanced()) cout<<"YES\n";
    else cout<<"NO\n";
    return 0;
}