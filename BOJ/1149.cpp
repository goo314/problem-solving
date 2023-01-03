#include <bits/stdc++.h>

using namespace std;

int arr[1000][3];

int red[1000];
int green[1000];
int blue[1000];

int main(){
    int n;
    cin >> n;

    for(int i=0; i<n; i++)
        for(int j=0; j<3; j++)
            cin >> arr[i][j];

    red[0] = arr[0][0];
    green[0] = arr[0][1];
    blue[0] = arr[0][2];

    for(int i=1; i<n; i++){
        red[i] = arr[i][0] + min(green[i-1], blue[i-1]);
        green[i] = arr[i][1] + min(red[i-1], blue[i-1]);
        blue[i] = arr[i][2] + min(red[i-1], green[i-1]);
    }

    cout << min(red[n-1], min(green[n-1], blue[n-1])) << endl;

}