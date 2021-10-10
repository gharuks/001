#include <iostream>
#include <cassert>
using namespace std;
struct node{
	int data;
	node *nxt=NULL;
	node(){
		data=0;
	}
	node(int _data){
		data=_data;
	}
	node(int _data, node *_nxt){
		data=_data;
		nxt=_nxt;
	}
};
struct linked_list{
	node *head=NULL;
	node* get_tail(){
		if(head==0)
			return 0;
		node *cur=head;
		while(cur->nxt!=0)
			cur=cur->nxt;
		return cur;
	}
	node* get(int i){
		node *cur=head;
		for(int j=0;j<i;j++){
			if(cur==0)
				return 0;
			cur=cur->nxt;
		}
		return cur;
	}
	void insert_begin(int data){
		node *new_node=new node(data, head);
		head=new_node;
	}
	void insert_tail(int data){
		node *tail=get_tail();
		node *new_node=new node(data);
		tail->nxt=new_node;
	}
	void insert(int i, int data){
		if(i==0){
			insert_begin(data);
			return;
		}
		node *A=get(i-1);
		if(A==0) {
			insert_tail(data);
			return;
		}
		node *B=A->nxt;
		node *new_node=new node(data, B);
		A->nxt=new_node;
	}
	void output(){
		cout<<"[";
		node *cur=head;
		while(cur!=0) {
			cout<<cur->data;
			cur=cur->nxt;
			if(cur==0)
				cout<<"]";
			else
				cout<<", ";
		}
		cout<<"\n";
	}
	void del_begin(){
		if(head==0)
			return;
		node *old_head=head;
		head=head->nxt;
		delete old_head;
	}
	void del_end(){
		if(head == 0)
			return;
		if(head->nxt == 0){ 
			delete head;
			head=0;
			return;
		}
		node *cur=head;
		while(cur->nxt->nxt!=0) 
			cur=cur->nxt;
		delete cur->nxt;
		cur->nxt=0;
	}
};
int main() {
	ifstream in("input.txt");
    out.open("output.txt");
    linked_list L;
    while (!in.eof()){
        string s;
        in>>s;
        if(s=="") continue;
        L.insert(s);
    }
    L.output();
    in.close();
    out.close();
}
