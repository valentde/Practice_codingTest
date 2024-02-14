/*
 (JS) 문자열 3개 입력 (\n)

    let [str1, str2, str3] = input;
    let [str1, str2, str3] = require("fs").readFileSync(0).toString().trim().split("\n");
 (C) 문자열 2개입력 (\n)
    scanf("%s\n%s\n%s", c1, c2, c3);i
 (C) 문자열 2번 출력 (\n)
    printf("%s\n%s", str, str);
*/

//[문자열 두번 출력하기 ](https://www.codetree.ai/missions/4/problems/print-string-twice)
#include <stdio.h>
int main() {
char s[100 + 1];
scanf("%s", s)
// 문자열을 두 번 출력 포맷
printf("%s\n%s", str, str);
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
//[더 긴 문자열 ](https://www.codetree.ai/missions/4/problems/longer-string)
#include <stdio.h>
#include <string.h>
int main() {
    char ch1[20], ch2[20];
    scanf("%s %s", ch1, ch2);
    int len1 = strlen(ch1);
    int len2 = strlen(ch2);

    if(len1 == len2){
        printf("same");
    } else if(len1 > len2){
        printf("%s %d", ch1, len1);
    }else{
        printf("%s %d", ch2, len2);
    }
    return 0;
}