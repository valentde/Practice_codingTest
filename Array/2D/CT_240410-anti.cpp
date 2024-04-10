//[격자 반대로 채우기 ](https://www.codetree.ai/missions/4/problems/grid-anti-fill)#include <iostream>
using namespace std;
int main() {
    int n, cnt=1;
    cin >> n;
    int grid[n][n];
    for(int i=0; i<n; i++) {
        if(i%2==0){
            for(int j=0; j<n; j++) grid[i][j] = i*n +1 + j;
        }else{
            for(int j=0; j<n; j++) grid[i][j] = (i+1)*n - j;
        }
    }

    //오른쪽 대각선 대칭
    for(int i=0; i<n; i++){
        for(int j=0; j<n - i; j++){
            int tmp = grid[i][j];
            grid[i][j] = grid[n -j -1][n -i -1];
            grid[n -j -1][n -i -1] = tmp;
        }
    }

    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) 
            cout<< grid[i][j] << " ";
            // printf("%3d", grid[i][j]);
        cout<<endl;
    }
}