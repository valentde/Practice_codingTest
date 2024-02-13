//  모든 점의 위치는 서로 겹치지 않음

//[격자에 점 그리기 ](https://www.codetree.ai/missions/4/problems/draw-points-on-grid)
#include <iostream>
using namespace std;
int main() {
    int n, m, grid[10][10] = {};
    cin >> n >> m;

    int r, c;
    for(int i=1; i<m+1; i++){
        cin>>r>>c;
        grid[r][c] = i;
    }

    for(int i=1; i<n+1; i++){
        for(int j=1; j<n+1; j++)
            cout << grid[i][j] << " ";
        cout << endl;
    }

    return 0;
}