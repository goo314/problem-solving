#include <bits/stdc++.h>

using namespace std;

char arr[5][5];

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int t;
    cin >> t;
    for(int x=1; x<=t; x++){
        int n, m; cin >> n >> m;
        string first;
        cin >> first;

        string ret = "yes";
        
        for(int i=1; i<n; i++){
            string arr;
            cin >> arr;

            int a, b;
            a = int(first[0]) - 48;

            if(int(arr[0])-48) b = !a;
            else b = a;

            for(int j=1; j<m; j++){
                a = int(first[j]) - 48;
                if((b^a) != (int(arr[j])-48)){
                    ret = "no";
                    break;
                }
            }
        }

        cout << "#" << x << " " << ret << endl;
        
    }
    
}