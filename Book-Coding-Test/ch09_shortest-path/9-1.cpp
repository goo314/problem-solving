#include <bits/stdc++.h>

using namespace std;

/*
#define INF 1e9 // 무한을 의미하는 값으로 10억을 설정

// 노드의 개수(N), 간선의 개수(M), 시작 노드 번호(Start)
// 노드의 개수는 최대 100,000개라고 가정
int n, m, start;
// 각 노드에 연결되어 있는 노드에 대한 정보를 담는 배열
vector<pair<int, int> > graph[100001];
// 최단 거리 테이블 만들기
int d[100001];

void dijkstra(int start) {
    priority_queue<pair<int, int> > pq;
    // 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    pq.push({0, start});
    d[start] = 0;
    while (!pq.empty()) { // 큐가 비어있지 않다면
        // 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        int dist = -pq.top().first; // 현재 노드까지의 비용 
        int now = pq.top().second; // 현재 노드
        pq.pop();
        // 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if (d[now] < dist) continue;
        // 현재 노드와 연결된 다른 인접한 노드들을 확인
        for (int i = 0; i < graph[now].size(); i++) {
            int cost = dist + graph[now][i].second;
            // 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if (cost < d[graph[now][i].first]) {
                d[graph[now][i].first] = cost;
                pq.push(make_pair(-cost, graph[now][i].first));
            }
        }
    }
}

int main(void) {
    cin >> n >> m >> start;

    // 모든 간선 정보를 입력받기
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        // a번 노드에서 b번 노드로 가는 비용이 c라는 의미
        graph[a].push_back({b, c});
    }

    // 최단 거리 테이블을 모두 무한으로 초기화
    fill(d, d + 100001, INF);
    
    // 다익스트라 알고리즘을 수행
    dijkstra(start);

    // 모든 노드로 가기 위한 최단 거리를 출력
    for (int i = 1; i <= n; i++) {
        // 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if (d[i] == INF) {
            cout << "INFINITY" << '\n';
        }
        // 도달할 수 있는 경우 거리를 출력
        else {
            cout << d[i] << '\n';
        }
    }
}
*/

vector<tuple<int, int>> g[100]; // g[v1] = (v2, w)
int dist[100];

int main(){
    int n, m, start; cin >> n >> m >> start;
    for(int i=0; i<m; i++){
        int v1, v2, w; cin >> v1 >> v2 >> w;
        g[v1-1].push_back({v2-1, w});
    }
    
    fill(dist, dist+100, 1e9);
    
    priority_queue<tuple<int, int>, vector<tuple<int, int>>, greater<>> pq; // (w, v)
    pq.push({0, start-1});
    dist[start-1] = 0;

    while(!pq.empty()){
        int w, v; tie(w, v) = pq.top(); pq.pop();
        if(dist[v] < w) continue;
        for(int i=0; i<g[v].size(); i++){
            int w2, v2; tie(v2, w2) = g[v][i];
            int nw = w + w2;
            if(nw < dist[v2]) {
                dist[v2] = nw;
                pq.push({nw, v2});
            }
        }
    }

    for(int i=0; i<n; i++){
        if(dist[i]==1e9) cout << "-1" << endl;
        else cout << dist[i] << endl;
    }

}
