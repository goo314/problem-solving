#include <bits/stdc++.h>

using namespace std;

int dp[1000];

int main(){

    int n;
    cin >> n;

    dp[0] = 1;
    dp[1] = 2;
    dp[2] = 3;
    
    for(int i=3; i<n; i++){
        dp[i] = (dp[i-1] + dp[i-2])%10007;
    }

    cout << dp[n-1] << endl;

}