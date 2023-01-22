#include < array >
#include < iostream >
#include < string >

struct Node {
	int key;
	Node *left, *right;
};

constexpr size_t MAX_NODE = 1000;

int node_count = 0;
Node node_pool[MAX_NODE];

Node* new_node(int x) {
	node_pool[node_count].key = x;
	node_pool[node_count].left = nullptr;
	node_pool[node_count].right = nullptr;

	return &node_pool[node_count++];
}

class BinarySearchTree {
	Node* root;

public:
	BinarySearchTree() = default;

	void init() {
		root = nullptr;
		node_count = 0;
	}

	void insert(int x) {
		root = insert_rec(root, x);
	}

	void remove(int x) {
		root = remove_rec(root, x);
	}

	bool find(int x) const {
		Node* node = root;
		while (node != nullptr) {
			if (node->key == x) {
				return true;
			}
			node = x < node->key ? node->left : node->right;
		}
		return false;
	}

	void traversal(int type) const {
		static constexpr std::array< const char*, 3> traversal_types = {"pre", "in", "post"};
		std::cout << traversal_types[type] << "-order  ";
		traversal_rec(root, type);
		std::cout << '\n';
	}

private:
	Node* insert_rec(Node* node, int x) {
		if (node == nullptr) {
			return new_node(x);
		}

		if (x < node->key) {
			node->left = insert_rec(node->left, x);
		} else if (x > node->key) {
			node->right = insert_rec(node->right, x);
		}

		return node;
	}

	Node* remove_rec(Node* node, int x) {
		if (node == nullptr) {
			return node;
		}

		if (x < node->key)
			node->left = remove_rec(node->left, x);
		else if (x > node->key)
			node->right = remove_rec(node->right, x);
		else {
			if (node->left == nullptr) {
				return node->right;
			} else if (node->right == nullptr) {
				return node->left;
			}
			const int temp = find_min_key(node->right);
			node->key = temp;
			node->right = remove_rec(node->right, temp);
		}

		return node;
	}

	int find_min_key(Node* node) const {
		while (node->left != nullptr) {
			node = node->left;
		}
		return node->key;
	}

	void traversal_rec(Node* node, int type) const {
		if (node == nullptr) return;
		if (type == 0) std::cout << node->key << ' ';
		traversal_rec(node->left, type);
		if (type == 1) std::cout << node->key << ' ';
		traversal_rec(node->right, type);
		if (type == 2) std::cout << node->key << ' ';
	}

	// 스택을 사용한 트리 순회
	void pre_order() {
		std::stack< Node*> stk;
		stk.emplace(root);

		std::cout << "pre-order  ";
		while (!stk.empty()) {
			const Node* node = stk.top();
			stk.pop();

			std::cout << node->key << ' ';

			if (node->right != nullptr) stk.emplace(node->right);
			if (node->left != nullptr) stk.emplace(node->left);
		}
		std::cout << '\n';
	}
};

int main() {
	BinarySearchTree tree;
	// 0   : 초기화
	// 1 x : x 삽입
	// 2 x : x 삭제
	// 3 x : x 탐색
	// 4 t : 순회 (t: 0 전위, 1 중위, 2 후위)
	int cmd, x;
	for (;;) {
		std::cin >> cmd;
		switch (cmd) {
		case 0:
			tree.init();
			break;
		case 1:
			std::cin >> x;
			tree.insert(x);
			break;
		case 2:
			std::cin >> x;
			tree.remove(x);
			break;
		case 3:
			std::cin >> x;
			std::cout << (tree.find(x) ? "found" : "not found") << '\n';
			break;
		case 4:
			std::cin >> x;
			if (x < 0 || x > 2) return std::cout << "invalid traversal type\n", 0;
			tree.traversal(x);
			break;
		default:
			return std::cout << "invalid command\n", 0;
		}
	}
}