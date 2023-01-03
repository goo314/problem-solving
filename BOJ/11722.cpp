#include <bits/stdc++.h>

using namespace std;

int arr[1001];
int dp[1001];

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int n;
    cin >> n;
    for(int i=0; i<n; i++) cin >> arr[i];

    int ret = 0;
    for(int i=0; i<n; i++){
        dp[i] = 1;
        for(int j=0; j<i; j++){
            if(arr[j] > arr[i]) dp[i] = max(dp[i], dp[j]+1);
        }
        if(ret < dp[i]) ret = dp[i];
    }
    
    cout << ret << endl;
    
}