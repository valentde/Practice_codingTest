//[지그재그로 숫자 채우기 ](https://www.codetree.ai/missions/4/problems/zigzag-numbering)

// [j][i] 아래쪽    → 우측 한 칸 → 위쪽 → 오른쪽 한 칸  → ...
// [i][j] 우측이동 → 아래 한 칸 → 좌측이동 → 아래 한 칸  → ...
#include <iostream>
using namespace std;
int main() {
    int n, m, arr[100][100], val=0;
    cin >> n >> m;
    for(int i=0; i<m; i++){
        if(i%2==0){
            for(int j=0; j<n; j++) arr[j][i] = val++;
        }else{
            for(int j=n-1; j>=0; j--) arr[j][i] = val++;
        }
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cout << arr[i][j] << " ";
        }
        cout<<endl;
    }
    return 0;
}