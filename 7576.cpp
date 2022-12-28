#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int m, n;
    cin >> m;
    cin >> n;

    queue< pair< pair<int, int>, int> > q;
    int cnt = 0;

    int arr[1000][1000];
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cin >> arr[i][j];
            cnt++;
            if(arr[i][j] == 1) {
                q.push(make_pair(make_pair(i, j), 0));
                cnt--;
            }
            if(arr[i][j] == -1) cnt--;
        }
    }
    
    int dx[4] = {0, 0, 1, -1};
    int dy[4] = {1, -1, 0, 0};
    int ret = 0;
    int d;
    
    while(!q.empty()){
        int x = q.front().first.first;
        int y = q.front().first.second;
        d = q.front().second;
        q.pop();
        for(int k=0; k<4; k++){
            int nx = x + dx[k];
            int ny = y + dy[k];
            int nd = d + 1;

            if(arr[nx][ny] == -1 || arr[nx][ny] == 1 || nx<0 || nx>=n || ny<0 || ny>=m) continue;
            q.push(make_pair(make_pair(nx, ny), nd));
            arr[nx][ny] = 1;
            cnt--;
        }
    }

    if(cnt != 0 ) cout << -1 << "\n";
    else cout << d << "\n";
    
    return 0;
}