//[단어로 구분하기 ](https://www.codetree.ai/missions/4/problems/separate-words-with-words)
#include <stdio.h>

int main() {
    char word[10][201];
    for(int i=0; i<10; i++) scanf("%s", word[i]);

    for(int i=0; i<10; i++) printf("%s\n", word[i]);
}
//[단어로 구분하기 2 ](https://www.codetree.ai/missions/4/problems/separate-words-with-words-2)
// 홀수번만 출력
int main() {
    char word[10][201];
    for(int i=0; i<10; i++) scanf("%s", word[i]);

    for(int i=0; i<10; i+=2) printf("%s\n", word[i]);
}
//[단어로 구분하기 3 ](https://www.codetree.ai/missions/4/problems/separate-words-with-words-3)
// 입력순서 반대 출ㄺ
int main() {
    char word[10][201];
    for(int i=0; i<10; i++) scanf("%s", word[i]);

    for(int i=9; i>=0; i--) printf("%s\n", word[i]);
}
