// [두 가지로 열리는 자물쇠 ](https://www.codetree.ai/missions/5/problems/a-two-way-lock)
/*
    내 풀이보다 해설이랑 토론이 더 나음

    🚩 3중 for문으로 [a,b,c] 조합의 개수 세기
    ⭕ n번째가 서로 독립적이니 (경우의수)x(경우의수)x(경우의수)

    bool -> can :  동작이 가능한지 여부를 판단
    수학적인 맥락에서 원(circle) vs 물리객체, 개념객체 원형이나 순환성질은  circular

 */
// 개수세는 조건이 헷갈려서 헤맴
#include <iostream>
#include <climits>
using namespace std;

// bool -> can :  동작이 가능한지 여부를 판단
// 수학적인 맥락에서 원(circle) vs 물리객체, 개념객체 원형이나 순환성질은  circular
bool CanUnlockCircularLock_falseNavie(int size, int num, int cond1, int cond2) {
    if ((num - cond1 + size) % size > 2) return false;
    if ((num - cond2 + size) % size > 2) return false;
    return true;
}

bool CanUNLockCircularLock(int size, int n[3], int c[3]) {
    for (int i = 0; i < 3; ++i) {
        // if ((n[i] + size - c[i]) % size <= 2)

        if (abs(n[i] - c[i]) <= 2) continue;

        // if (n[i] - c[i] > 0 && n[i] - c[i] > 2) return false; //  1000중 값 504

        int negative  = n[i] - c[i];
        if(negative >0 ) negative *= -1;
        if( (negative + size) % size >2 ) return false;

    }
    return true;
}

int main() {
    //잠김 앞뒤 2이내, 풀림(열림) 2초과
    int n3, a1, b1, c1, a2, b2, c2, oppositeLockCount = 0;

    cin >> n3 >> a1 >> b1 >> c1 >> a2 >> b2 >> c2;
    int condition1[3] = {a1, b1, c1};
    int condition2[3] = {a2, b2, c2};

    for (int i = 1; i < n3 + 1; ++i)
        for (int j = 1; j < n3 + 1; ++j)
            for (int k = 1; k < n3 + 1; ++k) {
                int arr[3] = {i, j, k};
                if (CanUNLockCircularLock(n3, arr, condition1) || CanUNLockCircularLock(n3, arr, condition2))
                    ++oppositeLockCount;
            }
    cout << oppositeLockCount;
}
