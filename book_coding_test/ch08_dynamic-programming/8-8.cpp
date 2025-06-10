#include <bits/stdc++.h>

using namespace std;

int arr[100];
int dp[10001];

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    memset(dp, 10001, sizeof(dp));

    int n, m;
    cin >> n >> m;
    for(int i=0; i<n; i++) {
        cin >> arr[i];
        // dp[arr[i]] = 1;
    }

    // for(int i=1; i<=m; i++){
    //     for(int j=0; j<n; j++){
    //         if(i-arr[j]<0 || !dp[i-arr[j]]) continue;
    //         dp[i] = min(dp[i], dp[i-arr[j]]+1);
    //     }
    // }

    dp[0] = 0;
    for(int i=0; i<n; i++){
        for(int j=arr[i]; j<=m; j++){
            if(dp[j-arr[i]<10001]) dp[j] = min(dp[j], dp[j-arr[i]]+1);
        }
    }
    
    if(dp[m]>=10001) cout << -1;
    else cout << dp[m];

}