#include < iostream >
#include < numeric >
#include < utility >
#include < vector >

void f0(int n, std::vector< std::pair< int, int >> edges) {
	// data
	std::vector< std::vector< int >> graph(n);
	// build
	for (const auto& e : edges) {
		graph[e.first].emplace_back(e.second);
	}
	// iterate
	std::cout << "using vector\n";
	for (int u = 0; u < n; ++u) {
		std::cout << u << " ->";
		for (const auto& v : graph[u]) {
			std::cout << ' ' << v;
		}
		std::cout << '\n';
	}
	std::cout << '\n';
}

void f1(int n, std::vector< std::pair< int, int >> edges) {
	// data
	struct LinkedListNode {
		int id;
		int next;
	};
	std::vector< LinkedListNode > nodes(edges.size());
	std::vector< int > head(n, -1);
	// build
	for (int i = 0; i < static_cast< int >(edges.size()); ++i) {
		nodes[i].id = edges[i].second;
		nodes[i].next = head[edges[i].first];
		head[edges[i].first] = i;
	}
	// iterate
	std::cout << "using linked list\n";
	for (int u = 0; u < n; ++u) {
		std::cout << u << " ->";
		for (int i = head[u]; i != -1; i = nodes[i].next) {
			std::cout << ' ' << nodes[i].id;
		}
		std::cout << '\n';
	}
	std::cout << '\n';
}

void f2(int n, std::vector< std::pair< int, int >> edges) {
	// data
	std::vector< int > outdegree(n);
	std::vector< int > prefix(n + 1);
	std::vector< int > vertices(edges.size());
	// build
	for (const auto& e : edges) {
		++outdegree[e.first];
	}
	std::partial_sum(outdegree.begin(), outdegree.end(), std::next(prefix.begin()));
	for (const auto& e : edges) {
		vertices[prefix[e.first] + --outdegree[e.first]] = e.second;
	}
	// iterate
	std::cout << "using prefix sum\n";
	for (int u = 0; u < n; ++u) {
		std::cout << u << " ->";
		for (int i = prefix[u]; i < prefix[u + 1]; ++i) {
			std::cout << ' ' << vertices[i];
		}
		std::cout << '\n';
	}
	std::cout << '\n';
}

int main() {
	constexpr int n = 5;
	const std::vector< std::pair< int, int >> edges =
		{{0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 4}, {3, 2}, {4, 3}};

	f0(n, edges);
	f1(n, edges);
	f2(n, edges);
}