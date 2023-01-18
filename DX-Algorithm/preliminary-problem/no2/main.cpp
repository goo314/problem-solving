#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int t; cin >> t;
    for(int test_case=1; test_case<=t; test_case++){
        string n;
        char x, y; cin >> n >> x >> y;

        int len = n.size(), size;

        cout << "#" << test_case << " ";
        if(len == 1){
            if(n[0] < x) cout << -1 << endl;
            else if(n[0] < y){
                if(x == '0') cout << -1 << endl;
                else cout << x << endl;
            }
            else cout << y << endl;
            continue;
        }

        int sublen;
        for(sublen=0; sublen<len; sublen++)
            if(n[sublen]!=x && n[sublen]!=y) break;

        if(sublen == len) cout << n << endl;

        else if(n[sublen]<x){
            while(n[--sublen]==x && sublen);
            if(sublen<0) cout << setfill(y) << setw(len-1) << y << endl;
            else if(n[sublen]==y) {
                if(!sublen && x=='0') cout << setfill(y) << setw(len-sublen-1) << y << endl;
                else cout << n.substr(0, sublen) << x << setfill(y) << setw(len-sublen-1) << y << endl;
            }
            else cout << n.substr(0, sublen) << setfill(y) << setw(len-sublen-1) << y << endl;
        }
        else if(n[sublen]<y){
            size = len - sublen - 1;
            if(!size){
                if(!sublen && x=='0') cout << -1 << endl;
                else cout << n.substr(0, sublen) << x << endl;
            }
            else{
                if(!sublen && x=='0') cout << setfill(y) << setw(size) << y << endl;
                else cout << n.substr(0, sublen) << x << setfill(y) << setw(size) << y << endl;
            }
        }
        else{
            size = len - sublen;
            if(!size) cout << n.substr(0, sublen) << y << endl;
            else cout << n.substr(0, sublen) << setfill(y) << setw(size) << y << endl;
        }

    }
    
}