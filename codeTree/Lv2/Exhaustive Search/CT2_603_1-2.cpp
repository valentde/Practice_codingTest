#include <iostream>
#include <climits>
using namespace std;

// [한 가지로 열리는 자물쇠 ](https://www.codetree.ai/missions/5/problems/one-way-lock)
int main1() {
    int n1, a, b, c, count=0;
    cin >> n1 >> a >> b >> c;

    //1부터 N까지 숫자를 중복해서 뽑아 총 3자리
    for (int i = 1; i < n1 + 1; ++i) for (int j = 1; j < n1 + 1; ++j) for (int k = 1; k < n1+1; ++k) {
        if(abs(i - a) <=2 || abs(j-b)<=2  || abs(k-c)<=2) count++;
    }
    cout << count;
}
// [개발자의 능력 3 ](https://www.codetree.ai/missions/5/problems/ability-of-developer-3)
int main2() {
    int capacity[6];
    int total=0;

    for (int i = 0; i < 6; ++i) {
        cin >> capacity[i];
        total += capacity[i] ;
    }
    int minDiff = INT_MAX;
    for (int i = 0; i < 6; ++i) for (int j = i+1; j < 6; ++j) for (int k = j+1; k < 6; ++k) {
        int sum = capacity[i] + capacity[j] + capacity[k];

        minDiff = min(minDiff, abs(total - sum - sum));
    }
    cout << minDiff;
}
