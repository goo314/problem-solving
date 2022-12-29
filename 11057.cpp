#include <bits/stdc++.h>

using namespace std;

int dp0[1000];
int dp1[1000];
int dp2[1000];
int dp3[1000];
int dp4[1000];
int dp5[1000];
int dp6[1000];
int dp7[1000];
int dp8[1000];
int dp9[1000];

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int n;
    cin >> n;

    dp0[0] = dp1[0] = dp2[0] = dp3[0] = dp4[0] = dp5[0] = dp6[0] = dp7[0] = dp8[0] = dp9[0] = 1;
    
    for(int i=1; i<n; i++){
        dp0[i] = dp0[i-1] %10007;
        dp1[i] = (dp0[i-1] + dp1[i-1])%10007;
        dp2[i] = (dp0[i-1] + dp1[i-1] + dp2[i-1])%10007;
        dp3[i] = (dp0[i-1] + dp1[i-1] + dp2[i-1] + dp3[i-1])%10007;
        dp4[i] = (dp0[i-1] + dp1[i-1] + dp2[i-1] + dp3[i-1] + dp4[i-1])%10007;
        dp5[i] = (dp0[i-1] + dp1[i-1] + dp2[i-1] + dp3[i-1] + dp4[i-1] + dp5[i-1])%10007;
        dp6[i] = (dp0[i-1] + dp1[i-1] + dp2[i-1] + dp3[i-1] + dp4[i-1] + dp5[i-1] + dp6[i-1])%10007;
        dp7[i] = (dp0[i-1] + dp1[i-1] + dp2[i-1] + dp3[i-1] + dp4[i-1] + dp5[i-1] + dp6[i-1] + dp7[i-1])%10007;
        dp8[i] = (dp0[i-1] + dp1[i-1] + dp2[i-1] + dp3[i-1] + dp4[i-1] + dp5[i-1] + dp6[i-1] + dp7[i-1] + dp8[i-1])%10007;
        dp9[i] = (dp0[i-1] + dp1[i-1] + dp2[i-1] + dp3[i-1] + dp4[i-1] + dp5[i-1] + dp6[i-1] + dp7[i-1] + dp8[i-1] + dp9[i-1])%10007;
    }

    int result = (dp0[n-1] + dp1[n-1] + dp2[n-1] + dp3[n-1] + dp4[n-1] + dp5[n-1] + dp6[n-1] + dp7[n-1] + dp8[n-1] + dp9[n-1])%10007;

    cout << result << endl;

}