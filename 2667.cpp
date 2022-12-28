#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n;
    cin >> n;
    char a[25][25];
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> a[i][j];
        }
    }

    queue< pair<int, int> > q;
    bool is_visited[25][25];
    //fill(is_visited, is_visited+25*25, false);
    memset(is_visited, 0, sizeof(is_visited));

    vector<int> ans;
    int cnt;

    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(a[i][j] == '1' && !is_visited[i][j]){
                cnt = 0;
                q.push(make_pair(i, j));
                is_visited[i][j] = true;
                while(!q.empty()){
                    int x = q.front().first;
                    int y = q.front().second;
                    q.pop();
                    cnt++;
                    for(int k=0; k<4; k++){
                        int nx = x + dx[k];
                        int ny = y + dy[k];
                        if(0<=nx && nx<n && 0<=ny && ny<n && !is_visited[nx][ny] && a[nx][ny] == '1'){
                            q.push(make_pair(nx, ny));
                            is_visited[nx][ny] = true;
                        }
                    }
                }
                ans.push_back(cnt);
            }
        }
    }
    sort(ans.begin(), ans.end());
    cout << ans.size() << "\n";
    for(int i=0; i<ans.size(); i++)
        cout << ans[i] << "\n";
    return 0;
}