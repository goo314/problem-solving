#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int t; cin >> t;
    for(int x=1; x<=t; x++){
        char str[10000]; cin >> str;

        for(int i=0; i<strlen(str); i++){
            cout << str[i];
        }
    }
    
}