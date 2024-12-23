// [개발자의 능력 2 ](https://www.codetree.ai/missions/5/problems/ability-of-developer-2)
/*
   2팀(반반) → 3팀
1) 오름차순 정렬 - 양끝
2) 4중 for문
    for i=0  ...n
    for j=i+1...n

    for k=0  ...n
    for l=k+1...n

    나머지 2팀합은 전체값에서 두팀 빼기
(JS) .reduce() = 합계, 남은 값
(C++) 3항 연산자 출력 에러
(JS) min, max 3개이상 비교 1줄처리
*/

#include <iostream>
#include <algorithm>

using namespace std;

int main5() {
    // 상수 6명
    int cap5[6];
    for (int i = 0; i < 6; ++i) cin >> cap5[i];

    sort(cap5, cap5 + 6);

    int maxSum=0, minSum=2000000;
    for (int i = 0; i < 6 / 2 ; ++i) {
        int s = cap5[i] + cap5[6 - i -1];
        minSum = min(minSum, s);
        maxSum = max(maxSum, s);
    }
    cout << maxSum - minSum;
}


// [개발자의 능력 2 ](https://www.codetree.ai/missions/5/problems/ability-of-developer-2)
/*
    min, max 3개이상 비교 1줄처리
    c++ 3항 연산자 출력 유의
*/

int main6() {
    int cap6[5] = {}, total = 0, minDiff = INT_MAX;
    for (int i = 0; i < 5; ++i) {
        cin >> cap6[i];
        total += cap6[i];
    }

    for (int x = 0; x < 5; ++x)
        for (int y = 0; y < 5; ++y)
            for (int z = y + 1; z < 5; z++) {
                if (x == y || x == z) continue;
                int sum1 = cap6[x];
                int sum2 = cap6[y] + cap6[z];
                int sum3 = total - sum2 - sum1;

                // 3개 중복 제외
                if (sum1 == sum2 || sum1 == sum3 || sum2 == sum3) continue;

                //3개 최대 최소 비교 → 1줄
                int maxCap = max(sum1, sum2);
                maxCap = max(maxCap, sum3);

                int minCap = min(sum1, sum2);
                minCap = min(minCap, sum3);

                if (minDiff > maxCap - minCap)
                    minDiff = maxCap - minCap;
            }
    // cout << (minDiff < 2000) ? minDiff : -1;
    cout << (minDiff == INT_MAX ? -1 : minDiff);
}