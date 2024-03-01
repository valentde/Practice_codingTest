#include <stdio.h>
#include <string.h>
int main() {
    char s[20 + 1 + 5];
    scanf("%s", s);

//    (1) 원시적...
    int len = strlen(s);
    s[len + 0] = 'H';
    s[len + 1] = 'e';
    s[len + 2] = 'l';
    s[len + 3] = 'l';
    s[len + 4] = 'o';
    s[len + 5] = '\0';

//  (2) 단어 문자열
    char hel[6] = "Hello";
    for(int i = 0; i < 5; i++)
        str[len + i] = hel[i];
	str[len + 5] = '\0';

    printf("%s", s);
}