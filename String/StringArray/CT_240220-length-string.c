//[문자열의 총 길이 구하기 ](https://www.codetree.ai/missions/4/problems/find-the-length-of-the-string)
/*  한 칸(' ') 구분 문자열 배열
    char str[10][201];
    for(int i = 0; i < 10; i++) scanf("%s", str[i]); // &없음!

    string str[10];
    for(int i = 0; i < 10; i++) std::cin >> str[i];

    str = input().split()

    String[] str = new String[10];
    for(int i = 0; i < 10; i++) str[i] = sc.next();

    let str = require("fs").readFileSync(0).toString().trim().split(" ");
*/
#include <stdio.h>
#include <string.h>
int main() {
    char str[10][201];
    for(int i=0; i<10; i++) scanf("%s", &str[i]); 

    int count=0;
    for(int i=0; i<10; i++) count += strlen(str[i]);

    printf("%d", count);
}