#include <cstdio>

struct Node {
	int data;
	Node* next;
};

constexpr size_t MAX_NODE = 1000;

int node_count = 0;
Node node_pool[MAX_NODE];

Node* new_node(int data) {
	node_pool[node_count].data = data;
	node_pool[node_count].next = nullptr;

	return &node_pool[node_count++];
}

class SinglyLinkedList {
	Node head;

public:
	SinglyLinkedList() = default;

	void init() {
		head.next = nullptr;
		node_count = 0;
	}

	void insert(int x) {
		Node* node = new_node(x);

		node->next = head.next;
		head.next = node;
	}

	void remove(int x) {
		Node* prev_ptr = &head;
		while (prev_ptr->next != nullptr && prev_ptr->next->data != x) {
			prev_ptr = prev_ptr->next;
		}

		if (prev_ptr->next != nullptr) {
			prev_ptr->next = prev_ptr->next->next;
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
};

int main() {
	SinglyLinkedList slist;
	int a, b;
	for (;;) {
		scanf("%d", &a);
		switch (a) {
		case 0:
			slist.init();
			slist.print();
			break;
		case 1:
			scanf("%d", &b);
			slist.insert(b);
			slist.print();
			break;
		case 2:
			scanf("%d", &b);
			slist.remove(b);
			slist.print();
			break;
		case 3:
			scanf("%d", &b);
			puts(slist.find(b) ? "found" : "not found");
			break;
		default:
			return puts("wrong input"), 0;
		}
	}
}