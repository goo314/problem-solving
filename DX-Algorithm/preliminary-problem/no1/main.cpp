#include <bits/stdc++.h>

using namespace std;

string arr[20];
bool _buy[3000000][26];

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    freopen("input.txt", "r", stdin);

    int t; cin >> t;
    for(int x=1; x<=t; x++){
        int r, c; cin >> r >> c;
        for(int i=0; i<r; i++) cin >> arr[i];

        queue<tuple<int, int, int>> q; // (x, y, idx)
        int pos = 0, ret = 1;
        q.push({0, 0, 0});
        for(int i=0; i<26; i++) _buy[0][i] = false;
        _buy[0][arr[0][0]-'A'] = true;

        int dx[4] = {0, 0, 1, -1};
        int dy[4] = {1, -1, 0, 0};

        while(!q.empty()){
            int x, y, idx;
            tie(x, y, idx) = q.front(); q.pop();
            if(ret == 26) break;
            pos %= 3000000;
            
            for(int i=0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(nx<0 || nx>=r || ny<0 || ny>=c) continue;
                
                if(!_buy[idx][arr[nx][ny]-'A']){
                    pos++;

                    int cnt = 0;
                    for(int i=0; i<26; i++) {
                        _buy[pos][i] = _buy[idx][i];
                        if(_buy[pos][i]) cnt++;
                    }
                    _buy[pos][arr[nx][ny]-'A'] = true;
                    cnt++;

                    if(ret < cnt) ret = cnt;

                    q.push({nx, ny, pos});
                }
            }
        }

        // cout << pos << endl;
        cout << "#" << x << " " << ret << endl;
        
    }
    return 0;
}