//[바구니 안의 사탕 2 ](https://www.codetree.ai/missions/5/problems/candy-in-the-basket-2)
// 완탐대신 누적합 배열(prefixSum)으로 풀이
// 중심점 c를 잘 잡아 [c-K, c+K] 구간에 있는 사탕의 수가 최대
#include <iostream>
using namespace std;

int main() {
    int n, K, maxSumCenter, a, b;
    int arr5[100 + 1] = {};

    cin >>n >>K;
    for(int i=0; i<n; i++){
        cin >>a>>b;
        arr5[b] += a;
    }

    int prefixSum[100 + 1] = {};
    prefixSum[0] = arr5[0];
    for(int i=1; i<101; i++) prefixSum[i] = prefixSum[i - 1] + arr5[i];

    maxSumCenter =0;
    for(int c=0; c<= 100; c++){
        if(c-K < 0 || c+K > 101) continue;
        int sum = prefixSum[c +K] - prefixSum[c - K] + arr5[c - K];
        if(maxSumCenter < sum)
            maxSumCenter = sum;
    }
    cout <<(maxSumCenter>0 ? maxSumCenter : prefixSum[100]);
}