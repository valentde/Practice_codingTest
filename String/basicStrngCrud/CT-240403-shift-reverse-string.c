#include <stdio.h>

//[문자열 한 칸씩 밀어내며 뒤집기 ](https://www.codetree.ai/missions/4/problems/shift-reverse-string)
int main() {
    char str[1000 + 1];
    int q, query, len=0;
    scanf("%s %d", str, &q);

    while(str[++len]);

    while(q-->0){
        scanf("%d", &query);
        if(query == 1){ // 한 칸씩 앞으로 당기기
            char leftEnd = str[0];
            for(int i=0; i<len - 1; i++) str[i] = str[i + 1];
            str[len - 1] = leftEnd;

        }else if(query == 2){// 한 칸씩 뒤로 밀기
            char rightEnd = str[len - 1];
            for(int i=len - 1; i>0; i--) str[i] = str[i - 1];
            str[0] = rightEnd;

        }else{ //좌우로 뒤집기
            int mid = len / 2;
            for(int i=0; i<mid; i++){
                char val = str[len -1 - i];
                str[len -1 - i] = str[i];
                str[i] = val; 
            }
        }

        printf("%s\n", str);
    }
}

//[규칙에 따라 밀기 ](https://www.codetree.ai/missions/4/problems/push-by-the-rules)
int main() {
    char front, back, str[100 + 1], cmd[100 + 1];
    int len, cmdSize=0;
    scanf("%s %s", str, cmd);

    while(str[++len] != '\0');
    while(cmd[++cmdSize]);

    for(int m=0; m<cmdSize; m++){
        if(cmd[m] == 'L'){
            char front = str[0];
            for(int i=0; i<len - 1; i++) str[i] = str[i + 1];
            str[len - 1] = front;
        }else{
            char back = str[len - 1];
            for(int i=len-1; i>0; i--) str[i] = str[i - 1];
            str[0] = back;
        }
    }
    printf("%s", str);
}

//[문자열 돌리기 ](https://www.codetree.ai/missions/4/problems/SPin-SPring)
// 오른쪽으로 한 글자씩 밀어서 출력하는 것을 L회 반복
int main() {
    char str[10 + 1];
    scanf("%s", str);
    printf("%s\n", str);

    int len = 0;
    // while(str[++len] != '\0');
    while(str[++len]);

    int loopi = len;
    while(loopi-- >0){

        char rightEnd = str[len - 1];
        for(int i=len-1; i>0; i--) str[i] = str[i - 1];
        str[0] = rightEnd;

        printf("%s\n", str);
    }

}