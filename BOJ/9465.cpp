#include <bits/stdc++.h>

using namespace std;

int arr1[100000];
int arr2[100000];

int _none[100000];
int _up[100000];
int _down[100000];


int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    
    int t, n;
    cin >> t;

    for(int x=0; x<t; x++)
    {
        cin >> n;
        for(int i=0; i<n; i++) cin >> arr1[i];
        for(int i=0; i<n; i++) cin >> arr2[i];

        _none[0] = 0;
        _up[0] = arr1[0];
        _down[0] = arr2[0];

        int result = max(_none[0], max(_up[0], _down[0]));
        for(int i=1; i<n; i++){
            _none[i] = max(_none[i-1], max(_up[i-1], _down[i-1]));
            _up[i] = arr1[i] + max(_none[i-1], _down[i-1]);
            _down[i] = arr2[i] + max(_none[i-1], _up[i-1]);

            int dp = max(_none[i], max(_up[i], _down[i]));
            if(result < dp) result = dp;
        }

        cout << result << endl;


    }

}