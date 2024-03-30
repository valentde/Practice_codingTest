//[문자열 밀기 ](https://www.codetree.ai/missions/4/problems/push-char)
#include <stdio.h>
#include <string.h>
int main() {
    char s[20 + 1];
    scanf("%s", s);
    int len = strlen(s);
    char first = s[0];
    for(int i=0; i<len -1; i++){
        s[i] = s[i + 1];
    }

    s[len -1] = first;
    printf("%s", s);

}