#include <bits/stdc++.h>

using namespace std;

struct Node {
    int key;
    int depth;
    Node *prev;
    Node *left, *right;
};

constexpr size_t MAX_NODE = 10001;

Node node_pool[MAX_NODE];

Node* new_node(int x) {
    node_pool[x].key = x;
    node_pool[x].prev = nullptr;
    node_pool[x].left = nullptr;
    node_pool[x].right = nullptr;
	return &node_pool[x];
}

void compute_depth(){
    queue<tuple<int, int>> q; // (index, depth)
    q.push({1, 0});

    while(!q.empty()){
        int x, d; tie(x, d) = q.front(); q.pop();
        Node* node = &node_pool[x];
        if(node->left){
            node->left->depth = d + 1;
            q.push({node->left->key, d+1});
        }
        if(node->right){
            node->right->depth = d + 1;
            q.push({node->right->key, d+1});
        }
    }
}

Node* common_parent(int p1, int p2){
    Node* node1 = &node_pool[p1];
    Node* node2 = &node_pool[p2];
    bool tmp = node1 != node2;
    while(node1 != node2){
        if(node1->depth < node2->depth) node2 = node2->prev;
        else node1 = node1->prev;
    }
    return node1;
}

int compute_subtree(Node* node, int num){
    if(node == nullptr) return 0;
    return compute_subtree(node->left, num) + num+1 + compute_subtree(node->right, num);
}

int main(){
    // ios::sync_with_stdio(false); cin.tie(nullptr);
    // freopen("input.txt", "r", stdin);

    int t; cin >> t;
    for(int tc=1; tc<=t; tc++){


        int v, e, p1, p2; cin >> v >> e >> p1 >> p2;

        // initilaize
        for(int i=1; i<=v; i++) Node* node = new_node(i);

        for(int i=0; i<e; i++){
            int p, c; cin >> p >> c;
            Node* parent = &node_pool[p];
            Node* child = &node_pool[c];
            child->prev = parent;
            if(!parent->left) parent->left = child;
            else parent->right = child;
        }

        compute_depth();
        
        printf("#%d ", tc);
        Node* subroot = common_parent(p1, p2); cout << subroot->key << " ";
        int ret = compute_subtree(subroot, 0); cout << ret << endl;
    }
}