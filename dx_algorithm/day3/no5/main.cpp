#include <bits/stdc++.h>

using namespace std;
#define MAX_NODE 10000

struct Node {
	int data;
	Node* prev;
	Node* next;
};

Node node[MAX_NODE];
int nodeCnt;
Node* head;

Node* getNode(int data) {
	node[nodeCnt].data = data;
	node[nodeCnt].prev = nullptr;
	node[nodeCnt].next = nullptr;
	return &node[nodeCnt++];
}

// 초기화
void init()
{
	head = new Node();
	head->prev = nullptr;
	head->next = nullptr;
	nodeCnt = 0;
}

// 맨 앞에 노드 추가
void addNode2Head(int data) 
{
	Node* node = getNode(data);
	node->next = head->next;
	node->prev = head;
	if(head->next) head->next->prev = node;
	head->next = node;
}

// 맨 뒤에 노드 추가
void addNode2Tail(int data) 
{
	Node* node = getNode(data);
	Node* ptr = head;
	while(ptr->next) ptr = ptr->next;
	node->prev = ptr;
	node->next = nullptr;
	ptr->next = node;
}

// 지정된 순서(num)에 노드 추가
void addNode2Num(int data, int num) 
{
	Node* node = getNode(data);
	Node* ptr = head;
	for(int i=0; i<num && ptr->next; i++) ptr = ptr->next;
	node->next = ptr->next;
	if(ptr->next) ptr->next->prev = node;
	node->prev = ptr;
	ptr->next = node;
}

void changeNode2Num(int data, int num) 
{
	Node* node = getNode(data);
	Node* ptr = head;
	for(int i=0; i<=num && ptr; i++) ptr = ptr->next;
    node->next = ptr->next;
    node->prev = ptr->prev;
    if(ptr->next) ptr->next->prev = node;
    ptr->prev->next = node;
}

// data를 가진 node 순서를 리턴
int findNode(int data) 
{
	Node* ptr = head;
	int num = 0;
	while(ptr->data!=data && ptr->next){
		ptr = ptr->next;
		num++;
	}
	return num;
}

// data를 가진 노드를 삭제
void removeNode(int num) 
{
	Node* ptr = head;
	for(int i=0; i<=num && ptr; i++) ptr = ptr->next;
    ptr->prev->next = ptr->next;
    if(ptr->next) ptr->next->prev = ptr->prev;
}

// 노드의 data 정보를 차례대로 output[]에 저장하고 노드 개수를 리턴
void printList() 
{
	Node* ptr = head->next;
	while(ptr) {
        cout << ptr->data << " ";
		ptr = ptr->next;
	}
    cout << endl;
}

void printData(int num)
{
    Node* ptr = head;
	for(int i=0; i<=num && ptr; i++) ptr = ptr->next;
    if(!ptr) cout << -1 << endl;
    else cout << ptr->data << endl;
}



int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    freopen("sample_input.txt", "r", stdin);

    int t; cin >> t;
    for(int tc=1; tc<=t; tc++){
        init();

        int n, m, l; cin >> n >> m >> l;
        for(int i=0; i<n; i++) {
            int x; cin >> x;
            addNode2Tail(x);
        }

        for(int i=0; i<m; i++){
            char cmd; cin >> cmd;
            int data, num;
            switch(cmd){
            case 'I':
                cin >> num >> data;
                addNode2Num(data, num);
                break;
            case 'D':
                cin >> num;
                removeNode(num);
                break;
            case 'C':
                cin >> num >> data;
                changeNode2Num(data, num);
                break;
            }
        }

        cout << "#" << tc << " ";
        printData(l);
    }
    
}