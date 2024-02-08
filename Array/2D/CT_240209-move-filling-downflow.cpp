//모범답안 :  [i][j] i+1 + n*(j)  --> [j][i] val++ [대칭으로 세로증가]

//[아래로 사각형 채우기 ](https://www.codetree.ai/missions/4/problems/filling-rectangle-with-downflow)
#include <iostream>
using namespace std;
int main() {
    int n, arr[10][10], val=0;
    cin >> n ;
    for(int i=0; i<n; i++) for(int j=0; j<n; j++) 
//            arr[i][j] = i+1 + n*(j);
			arr[j][i] = val++;

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout << arr[i][j] << " ";
        }
        cout<<endl;
    }
    return 0;
}