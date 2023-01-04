#include <bits/stdc++.h>

using namespace std;

int dp[31][31];

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);

    dp[0][0] = 1;
    dp[1][0] = 1;
    dp[1][1] = 1;

    for(int i=2; i<=30; i++){
        dp[i][0] = 1;
        dp[i][i] = 1;
        for(int j=1; j<i; j++){
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
        }
    }

    int t; cin >> t;
    for(int x=1; x<=t; x++){
        int n, m; cin >> n >> m;
        cout << dp[m][n] << endl;
    }
    
}