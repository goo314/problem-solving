#include <bits/stdc++.h>

using namespace std;

int dp[1000001];
int _prev[1000001];

int main() {
    int n;
    cin >> n;

    dp[1] = 0;
    _prev[1] = -1;

    dp[2] = 1;
    _prev[2] = 1;

    dp[3] = 1;
    _prev[3] = 1;

    for(int i=4; i<=n; i++){
        int _three = 1e9, _two = 1e9, _one = 1e9, __one = 1e9;

        if(i%3==0) _three = dp[i/3]+1;
        if(i%2==0) _two = dp[i/2]+1;
        _one = dp[i-1]+1;

        dp[i] = min(_three, min(_two, min(_one, __one)));
        if(dp[i] == _three) _prev[i] = i/3;
        if(dp[i] == _two) _prev[i] = i/2;
        if(dp[i] == _one) _prev[i] = i-1;
    }

    cout << dp[n] << endl;
    while(n != -1){
        cout << n << " ";
        n = _prev[n];
    }

}