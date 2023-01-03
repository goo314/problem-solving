#include <bits/stdc++.h>

using namespace std;

int arr[1000];

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int t = 10;
    for(int x=1; x<=t; x++){
        int n; cin >> n;
        for(int i=0; i<n; i++) cin >> arr[i];

        int ret = 0;
        for(int i=2; i<n-2; i++){
            ret += max(0, min(arr[i]-arr[i-1], min(arr[i]-arr[i-2], min(arr[i]-arr[i+1], arr[i]-arr[i+2]))));
        }
        
        printf("#%d %d\n", x, ret);
    }
    
}