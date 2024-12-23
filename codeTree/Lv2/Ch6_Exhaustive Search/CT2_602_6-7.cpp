// [G or H 2 ](https://www.codetree.ai/missions/5/problems/G-or-H-2)
/*
     for (int size = MAX; size >= 0; size--) { 사이즈 기준 X
      모두G or H 이면 변동 크기이므로 다른쪽 0
      모든배열이 G,H사이에 입력안된 0값도 있어서 안맞음
     (cpp) char[]배열 초기값 0
     (cpp) char은 "" 틀린다... 작음따음표
*/
#include <iostream>
#include <climits>
#define MAX 101
using namespace std;

int main6() {
    int n, maxSize = 0, cntG = 0, cntH = 0;
    char arr6[MAX] = {}; // char[]배열 초기값 0
    // int arr6[MAXARRSIZE] = {};

    cin >> n;
    for (int i = 0; i < n; i++) {
        int pos;
        char ch;
        cin >> pos >> ch;
        arr6[pos] = ch;
        // if(ch == "G") cntG++; char은 "" 틀린다... 작음따음표
        // if(ch == "H") cntH++;
    }

    // for (int size = MAX; size >= 0; size--) { 사이즈 기준 X
    for (int i = 0; i < MAX; i++) {
        if (arr6[i] == 0) continue; // 공백이면 넘기기 중요
        cntG = 0;
        cntH = 0;
        // for (int i = 0; i < size; i++) {
        for (int j = i; j < MAX; j++) {
            // if (arr6[i] == 'G') cntG++; // i 아니고 j
            // if (arr6[i] == 'H') cntH++;
            if (arr6[j] == 0) continue; // 공백이면 넘기기 중요
            if (arr6[j] == 'G') cntG++;
            if (arr6[j] == 'H') cntH++;

            // if (n == cntG || n == cntH || cntG == cntH) { 모두G or H 이면 변동 크기이므로 다른쪽 0
            // int size = j - i + 1; if (size == cntH || size == cntG ||  cntG == cntH) { 모든배열이 G,H사이에 입력안된 0값도 있어서 안맞음
            if (0 == cntH || 0 == cntG ||  cntG == cntH) {
                // maxSize = size;
                // break;
                maxSize = (j - i) > maxSize ? (j - i) : maxSize;
            }
        }
    }
    cout << (n == 1 ? 0 : maxSize);
}

//[밭의 높이를 고르게하기 ](https://www.codetree.ai/missions/5/problems/equalizing-the-height-of-the-field)
/*
    (기존)for 3개 : i=시작, j=끝, k=시작~끝
    (발전)for 2개
    ⭕한칸마다 계산해서 누적합
    ❌ 전체 배열값 누적 - 목표값 한번에 빼기
 */
int main7() {
    int N, H, T, minCost = INT_MAX;
    cin >> N >> H >> T;
    int field[N];
    for (int i = 0; i < N; i++) cin >> field[i];

    // i=시작, j=끝, k=시작~끝
    for (int i = 0; i < N; i++) {
        for (int j = i + T - 1; j < N; j++) {
            int levelSum = 0;
            for (int k = i; k < j + 1; ++k) levelSum += abs(H  - field[k]);

            minCost = min(minCost, levelSum);
        }
    }
    cout << minCost;
}
