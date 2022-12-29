#include <bits/stdc++.h>

using namespace std;

int _none[100000];
int _left[100000];
int _right[100000];

int dp[100000];

int main(){
    int n;
    cin >> n;

    dp[0] = 3;
    
    _none[0] = 1;
    _left[0] = 1;
    _right[0] = 1;

    for(int i=1; i<n; i++){

        _none[i] = (_left[i-1] + _right[i-1] + _none[i-1])%9901;
        _left[i] = (_none[i-1] + _right[i-1])%9901;
        _right[i] = (_none[i-1] + _left[i-1])%9901;

        dp[i] = (_none[i] + _left[i] + _right[i])%9901;

    }

    cout << dp[n-1] << endl;
}