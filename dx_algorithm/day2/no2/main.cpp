#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int t; cin >> t;
    for(int x=1; x<=t; x++){
        int n, m; cin >> n >> m;
        
        cout << "#" << x << " ";
        if((m & ((1<<n) -1)) == (1<<n)-1) cout << "ON";
        else cout << "OFF";
        cout << endl;
    }
}