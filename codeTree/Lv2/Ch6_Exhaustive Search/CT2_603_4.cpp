//[숫자 카운트 ](https://www.codetree.ai/missions/5/problems/numeric-count)
/*
    😡숫자후보 - 입력값으로 범위설정 삽질
    😆 3자리 자연수 완탐

    세자릿수 분해
    - 서로다른 숫자 걸러내기
    - 3자릿수 분해방법 (loop 제외)
    x : a의 백의 자릿수, y : 십의 자릿수, z : 일의 자릿수
    const x = Math.floor(a / 100);
    const y = Math.floor(a / 10) % 10;
    const z = a % 10;

    (JS) 순회 forLetOf - e 대신 [v1,v2]
*/
#include <iostream>
#include <algorithm>
using namespace std;

bool MatchNumber(int i, int j, int k, int *b) {
    int cnt1 = 0, cnt2 = 0, numB = b[0];
    if (numB % 10 == k) ++cnt1;
    else if (numB % 10 == i || numB % 10 == j) ++cnt2;

    // 2번째 자리수 표현 b[0] /10 %10;
    numB /= 10;
    if (numB % 10 == j) ++cnt1;
    else if (numB % 10 == i || numB % 10 == k) ++cnt2;

    numB /= 10;
    if (numB == i) ++cnt1;
    else if (numB == j || numB == k) ++cnt2;


    return (cnt1 == b[1] && cnt2 == b[2]);
}

int main4() {
    int n4, count4 = 0;
    cin >> n4;
    int arrB[n4][3];

    for (int i = 0; i < n4; i++) {
        cin >> arrB[i][0];
        cin >> arrB[i][1];
        cin >> arrB[i][2];
    }

    // 서로 다른 3자리 자연수 완전탐색
    for (int i = 1; i < 10; ++i)
        for (int j = 1; j < 10; ++j) {
            if (i == j) continue;
            for (int k = 1; k < 10; ++k) {
                if (k == i || k == j) continue; //504개
                bool isMatch = true;
                for (int m = 0; m < n4; ++m) {
                    if (MatchNumber(i, j, k, arrB[m]) == false) {
                        isMatch = false;
                        break;
                    }
                }
                if (isMatch) ++count4;
            }
        } //for-j
    cout << count4;
}