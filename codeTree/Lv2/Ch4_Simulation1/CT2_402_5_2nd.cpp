//2024-12-23(월)
// [진수 to 진수 ](https://www.codetree.ai/missions/5/problems/transformation-of-number-system)
#include<iostream>
#include <algorithm>  // std::reverse 함수가 정의된 헤더

using namespace std;
/*
질문
    진법에서 base와 radix 차이? 동일한 의미로, 특정 숫자 시스템이 몇 개의 숫자를 사용하는지

복습
    num → char 변환
    2-1. 동적배열
    2-2. 문자열 추가
        C++ : 누적합 += to_string() | std::reverse( .비긴, .엔드')
        JS : 동적배열 | .reverse().join("")
 */


int main() {
    // int aBase, bBase, num = 0;
    int aBase, bBase;
    string numStr;
    cin >> aBase >> bBase >> numStr;

    int deciNum =0;
    for(char i=0; i<numStr.length(); i++) {
        deciNum *= aBase;
        deciNum += (numStr[i] - '0');
    }

    string ansStrBaseB;
    while(deciNum > 0) {
        // bRadixNum += deciNum % bBase;
        ansStrBaseB += std::to_string(deciNum % bBase);
        deciNum /= bBase;
    }

    std::reverse(ansStrBaseB.begin(), ansStrBaseB.end());

    cout << ansStrBaseB << endl; ;
}
