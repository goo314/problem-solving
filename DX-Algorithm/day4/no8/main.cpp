#include <bits/stdc++.h>

using namespace std;

constexpr size_t MAX_NODE = 1000;
char node[MAX_NODE];

void in_order(int k, int n){
    if(k<=n){
        in_order(2*k, n);
        cout << node[k];
        in_order(2*k+1, n);
    }
}

int main(){
    // ios::sync_with_stdio(false); cin.tie(nullptr);
    // freopen("input.txt", "r", stdin);

    int t = 10;
    for(int tc=1; tc<=t; tc++){

        int n; cin >> n;
        
        for(int i=1; i<=n; i++){
            int idx; char key; int c1, c2;
            scanf("%d", &idx); scanf(" %c", &key);
            if(n%2==0 && i==n/2) cin >> c1;
            else if(i < n/2+1) cin >> c1 >> c2;
            node[idx] = key;
        }

        printf("#%d ", tc); in_order(1, n); cout << endl;
    }
}