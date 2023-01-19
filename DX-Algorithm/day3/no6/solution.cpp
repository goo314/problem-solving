#define MAX_NODE 10000

struct Node {
	int data;
	Node* next;
};

Node node[MAX_NODE];
int nodeCnt;
Node* head;

Node* getNode(int data) {
	node[nodeCnt].data = data;
	node[nodeCnt].next = nullptr;
	return &node[nodeCnt++];
}

void init()
{
	head = new Node();
    head->next = nullptr;
	nodeCnt = 0;
}

void addNode2Head(int data) 
{
	Node* node = getNode(data);
	node->next = head->next;
	head->next = node;
}

void addNode2Tail(int data) 
{
	Node* node = getNode(data);
	Node* ptr = head;
	while (ptr->next) ptr = ptr->next;
	node->next = ptr->next;
	ptr->next = node;
}

void addNode2Num(int data, int num) 
{
	Node* node = getNode(data);
	Node* ptr = head;
	for(int i=1; i<num && ptr->next; i++) ptr = ptr->next;
	node->next = ptr->next;
	ptr->next = node;
}

void removeNode(int data) 
{
	Node* ptr = head;
	while (ptr->next && ptr->next->data != data) ptr = ptr->next;
	if(ptr->next) ptr->next = ptr->next->next;
}

int getList(int output[MAX_NODE]) 
{
	Node* ptr = head->next;
	int i = 0;
	while(ptr) {
		output[i++] = ptr->data;
		ptr = ptr->next;
	}
	return i;
}