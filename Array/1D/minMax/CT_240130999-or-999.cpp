// [999 또는 -999 ](https://www.codetree.ai/missions/4/problems/999-or-999)
// 입력 중단값
#include <iostream>
#include <climits>
using namespace std;

int main() {
    int arr[100];
    int min=INT_MAX, max=INT_MIN; 

    for(int i=0; i<100; i++){
        cin >> arr[i];
        if(arr[i] == -999 || arr[i] == 999) break;

        if(arr[i] > max) max=arr[i]; 
        if(arr[i] < min) min=arr[i];
    }

    cout << max << " " << min << endl;
    return 0;
}