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

// 지정된 순서(num)에 노드 추가 (1 - 2 - 3 - 4 - 5 ...)
void addNode2Num(int data, int num) 
{
	Node* node = getNode(data);
	Node* ptr = head;
	for(int i=1; i<num && ptr->next; i++) ptr = ptr->next;
	node->next = ptr->next;
	if(ptr->next) ptr->next->prev = node;
	node->prev = ptr;
	ptr->next = node;
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
void removeNode(int data) 
{
	Node* ptr = head->next;
	while(ptr->data != data && ptr->next) ptr = ptr->next;
	if(ptr->data != data) return;
	if(ptr->next) ptr->next->prev = ptr->prev;
	ptr->prev->next = ptr->next;
}

// 노드의 data 정보를 차례대로 output[]에 저장하고 노드 개수를 리턴
int getList(int output[MAX_NODE]) 
{
	Node* ptr = head->next;
	int num = 0;
	while(ptr) {
		output[num++] = ptr->data;
		ptr = ptr->next;
	}
	return num;
}

// 노드의 data 정보를 역순으로 output[]에 저장하고 노드 개수를 리턴
int getReversedList(int output[MAX_NODE]) 
{
	Node* ptr = head;
	while(ptr->next) ptr = ptr->next;
	int num = 0;
	while(ptr!=head){
		output[num++] = ptr->data;
		ptr = ptr->prev;
	}
	return num;
}