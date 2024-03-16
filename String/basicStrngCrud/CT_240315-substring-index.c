//[부분문자열 위치 구하기 ](https://www.codetree.ai/missions/4/problems/find-location-of-substring)
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
int main() {

    char input[1001], target[1001];
    scanf("%s", input);
	scanf("%s", target);
    int lenInput=strlen(input), lenTarget = strlen(target);

    for(int i=0; i<lenInput - lenTarget + 1; i++){
        bool isMatch=true;
        for(int j=0; j<lenTarget; j++)
            if(input[i + j] != target[j]) isMatch = false;
        if(isMatch){
            printf("%d", i);
            return 0;
        }

    }

    printf("%d", -1);
    return 0;
}