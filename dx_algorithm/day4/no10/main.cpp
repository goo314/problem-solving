#include <bits/stdc++.h>

using namespace std;

struct Node {
	string key;
	Node *left, *right;
};

constexpr size_t MAX_NODE = 1000;

int node_count = 1;
Node node_pool[MAX_NODE];

Node* new_node(string x) {
	node_pool[node_count].key = x;
	node_pool[node_count].left = nullptr;
	node_pool[node_count].right = nullptr;

	return &node_pool[node_count++];
}

int traversal_rec(Node* node) {

    if(node->left == nullptr || node->right == nullptr) return stoi(node->key);

    // cout << traversal_rec(node->left) << node->key << traversal_rec(node->right) << endl;

    switch(node->key[0]){
    case '+':
        return  traversal_rec(node->left) + traversal_rec(node->right);
    case '-':
        return  traversal_rec(node->left) - traversal_rec(node->right);
    case '*':
        return  traversal_rec(node->left) * traversal_rec(node->right);
    case '/':
        return  traversal_rec(node->left) / traversal_rec(node->right);
    }
    return 0;
}


int main(){
    // ios::sync_with_stdio(false); cin.tie(nullptr);
    // freopen("input.txt", "r", stdin);
    int t = 10;
    for(int tc=1; tc<=t; tc++){
        node_count = 1;

        int n; cin >> n;
        for(int i=1; i<=n; i++){
            int idx; string key; int c1, c2;
            cin >> idx >> key;

            Node* node = new_node(key);

            if(key[0]-'0'<0){
                cin >> c1 >> c2;
                node->left = &node_pool[c1];
                node->right = &node_pool[c2];
            }
        }
        printf("#%d ", tc);
        int ret = traversal_rec(&node_pool[1]);
        cout << ret << endl;
    }

}