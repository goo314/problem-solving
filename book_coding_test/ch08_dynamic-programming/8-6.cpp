#include <bits/stdc++.h>

using namespace std;

int arr[100];
// int _taken[100];
// int _none[100];
int dp[100];

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    
    for(int i=0; i<n; i++) cin >> arr[i];

    // _taken[0] = arr[0];
    // _none[0] = 0;

    dp[0] = arr[0];
    dp[1] = max(arr[0], arr[1]);


    // int ret = 0;
    // for(int i=1; i<n; i++){
    //     _taken[i] = _none[i-1] + arr[i];
    //     _none[i] = max(_none[i-1], _taken[i-1]);
        
    //     if(ret < _taken[i]) ret = _taken[i];
    //     if(ret < _none[i]) ret = _none[i];
    // }
    // cout << ret << endl;
    
    for(int i=2; i<n; i++){
        dp[i] = max(dp[i-2]+arr[i], dp[i-1]);
    }
    cout << dp[n-1] << endl;

}