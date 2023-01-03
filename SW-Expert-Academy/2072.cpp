#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int t;
    cin >> t;
    
    for(int x=1; x<=t; x++){

        int ret = 0;
        for(int i=0; i<10; i++) {
            int n; cin >> n;
            if(n%2) ret += n;
        }
        cout << "#" << x << " " << ret << endl;
    }

    return 0;
    
}