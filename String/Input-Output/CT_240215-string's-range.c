/*
문자열 길이 ++증감함수
    ❌ while(s1[count++] != '\0');
    ⭕ while(s1[++count] != '\0');

3개 값 max, min - 3항 방정식
*/

//[가장 짧은 문자열 ](https://www.codetree.ai/missions/4/problems/shortest-string)
#include <stdio.h>
#include <string.h>
int main() {
    char c1[20], c2[20], c3[20];
    scanf("%s\n%s\n%s", c1, c2, c3);
    int len1 = strlen(c1), len2=strlen(c2), len3=strlen(c3);

    int maxLen = (len1 > len2 ? len1 : len2 > len3 ? len2 : len3);
    int minLen = (len1 < len2 ? len1 : len2 < len3 ? len2 : len3);

    printf("%d", maxLen - minLen);
}

//[문자열의 길이 출력하기 ](https://www.codetree.ai/missions/4/problems/print-string's-range)
#include <stdio.h>
#include <string.h>

int main() {
    char s1[100], s2[100];

    scanf("%s", s1);
    scanf("%s", s2);

    int count=0;
    // while(s1[count++] != '\0');
    while(s1[++count] != '\0');

    count += strlen(s2);


    printf("%d", count);
    return 0;
}