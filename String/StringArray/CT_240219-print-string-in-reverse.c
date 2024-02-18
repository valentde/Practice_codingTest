// console 입력) 공백 구분 문자열 
// [문자열 역순으로 출력하기 ](https://www.codetree.ai/missions/4/problems/print-string-in-reverse)
//  입력
//  Orange
//  Black
//  Purple
//  White

#include <stdio.h>
int main() {
    // char[] word[4]; 🙁 C랑 C++ 헷갈림;;
    char word[4][20 + 1];
    for(int i=0; i<4; i++) scanf("%s", word[i]);
    for(int i=0; i<4; i++) printf("%s\n", word[4 -i -1]);
    return 0;
}