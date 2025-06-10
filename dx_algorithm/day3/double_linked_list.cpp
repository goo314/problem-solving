#include <cstdio>

struct Node {
	int data;
	Node* prev;
	Node* next;
};

constexpr size_t MAX_NODE = 1000;

int node_count = 0;
Node node_pool[MAX_NODE];

Node* new_node(int data) {
	node_pool[node_count].data = data;
    node_pool[node_count].prev = nullptr;
	node_pool[node_count].next = nullptr;

	return &node_pool[node_count++];
}

class DoublyLinkedList {
	Node head;

public:
	DoublyLinkedList() = default;

	void init() {
        head = new Node();
        head.prev = nullptr;
		head.next = nullptr;
		node_count = 0;
	}

	void insert(int x) {
		Node* node = new_node(x);

		node->next = head.next;
        node->prev = head;
        if(head.next) head.next->prev = node;
		head.next = node;
	}

	void remove(int x) {
        Node* ptr = head.next;
	    while(ptr->data != data && ptr->next) ptr = ptr->next;
        if(ptr->data != data) return;
        if(ptr->next) ptr->next->prev = ptr->prev;
        ptr->prev->next = ptr->next;
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
};

int main() {
	DoublyLinkedList dlist;
	int a, b;
	for (;;) {
		scanf("%d", &a);
		switch (a) {
		case 0:
			dlist.init();
			dlist.print();
			break;
		case 1:
			scanf("%d", &b);
			dlist.insert(b);
			dlist.print();
			break;
		case 2:
			scanf("%d", &b);
			dlist.remove(b);
			dlist.print();
			break;
		case 3:
			scanf("%d", &b);
			puts(dlist.find(b) ? "found" : "not found");
			break;
		default:
			return puts("wrong input"), 0;
		}
	}
}