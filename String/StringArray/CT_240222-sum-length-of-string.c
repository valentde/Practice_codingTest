//[문자열 길이의 합 ](https://www.codetree.ai/missions/4/problems/sum-length-of-string)
#include <stdio.h>

int main() {
    int n, cntFirstA=0, i, sumLen=0;
    scanf("%d", &n);

    while(n-->0){
        char word[101];
        scanf("%s", word);

        cntFirstA += (word[0]=='a') ? 1 : 0;

        i=0;
        while(word[++i] != '\0');
        sumLen += i;
    }

    printf("%d %d", sumLen, cntFirstA);
    return 0;
}