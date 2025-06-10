#include <bits/stdc++.h>

using namespace std;

int dp[30001];

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    
    int x; cin >> x;

    dp[1] = 0;
    dp[2] = 1;
    dp[3] = 1;
    dp[4] = 2;
    dp[5] = 1;

    for(int i=6; i<=x; i++){
        int a = 1e9, b = 1e9, c = 1e9, d = 1e9;
        
        if(!(i%5)) a = dp[i/5];
        if(!(i%3)) b = dp[i/3];
        if(!(i%2)) c = dp[i/2];
        d = dp[i-1];
    }

    cout << dp[x] << endl;
}