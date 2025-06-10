// RUNTIME ERROR (Segmentation Fault!!)

#include <bits/stdc++.h>

using namespace std;

struct Node {
	int data;
	Node* next;
};

constexpr size_t MAX_NODE = 100000;

int node_count = 0;
Node node_pool[MAX_NODE];

Node* new_node(int data) {
	node_pool[node_count].data = data;
	node_pool[node_count].next = nullptr;

	return &node_pool[node_count++];
}

class SinglyLinkedList {
	Node head;
    Node* tail;

public:
	SinglyLinkedList() = default;

	void init() {
		head.next = nullptr;
        tail->next = nullptr;
		node_count = 0;
	}

	void insert(int x) {
		Node* node = new_node(x);
        if(!head.next) head.next = node;
        tail->next = node;
        tail = node;
	}

    // when "I x, y, s", insert s after x
    void insert(int x, int s){
        Node* node = new_node(s);
        
        if(!head.next) {
            head.next = node; return;
        }

        Node* prev_ptr = &head;
        for(int i=0; i<x; i++) prev_ptr = prev_ptr->next;

        if(!prev_ptr->next) tail = node;
        node->next = prev_ptr->next;
        prev_ptr->next = node;
    }

    // when "D x, y", delete y nodes after x
    void remove(int x, int y){

        Node* prev_ptr = &head;
        for(int i=0; i<x; i++) prev_ptr = prev_ptr->next;

        Node* next_ptr = prev_ptr;
        for(int i=0; i<y; i++) next_ptr = next_ptr->next;

        if(prev_ptr->next != nullptr){
            if(!next_ptr->next) tail = prev_ptr;
            prev_ptr->next = next_ptr->next;
        }

    }

	bool find(int x) const {
		Node* ptr = head.next;
		while (ptr != nullptr && ptr->data != x) {
			ptr = ptr->next;
		}

		return ptr != nullptr;
	}

	void print() const {
		Node* ptr = head.next;
		printf("[List] ");
		while (ptr != nullptr) {
			printf("%d", ptr->data);
			if (ptr->next != nullptr) {
				printf(" -> ");
			}
			ptr = ptr->next;
		}
		putchar('\n');
	}

    void print10() const {
        Node* ptr = head.next;
        for(int i=0; i<10; i++){
            printf("%d ", ptr->data);
            ptr = ptr->next;
        }
        putchar('\n');
    }
};

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);

    freopen("input.txt", "r", stdin);
    
    SinglyLinkedList slist;
    
    int t = 10;
    for(int tc=1; tc<=t; tc++){
        slist.init();
        
        int n; cin >> n;
        for(int i=0; i<n; i++){
            int x; cin >> x;
            slist.insert(x);
        }

        int m; cin >> m;
        for(int i=0; i<m; i++){
            char cmd; cin >> cmd;
            int x, y, s;
            switch(cmd){
            case 'I':
                cin >> x >> y;
                for(int j=0; j<y; j++){
                    cin >> s;
                    slist.insert(x+j, s);
                }
                break;
            case 'D':
                cin >> x >> y;
                slist.remove(x, y);
                break;
            case 'A':
                cin >> y;
                for(int j=0; j<y; j++){
                    cin >> s;
                    slist.insert(s);
                }
                break;
            default:
                break;
            }
        }

        printf("#%d ", tc); slist.print10();
    }
}