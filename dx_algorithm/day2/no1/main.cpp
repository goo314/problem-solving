#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int t; cin >> t;
    for(int x=1; x<=t; x++){
        int n; cin >> n;

        int digit[10] = {0, };
        int cnt = 0;
        
        int ret;
        for(int i=0; cnt<10; i++){
            ret = n*i;
            
            int tmp = ret;
            while(tmp>0){
                if(!digit[tmp%10]) cnt++;
                digit[tmp%10] = 1;
                tmp /= 10;
            }
        }

        cout << "#" << x << " " << ret << endl;
    }
    
}