# [문자열 범위 출력 2 ](https://www.codetree.ai/missions/4/problems/print-string-in-range-2)
word = input()
n = int(input())

# 3항 방정식 없으면 Runtime Error
# [len(word) - 1 - i] 인덱스 범위 초과
# FunLeeBrosCode
# 100
n = ( len(word) if len(word) < n else n )

for i in range(n):
    print( word[len(word) - 1 - i], end='')

# # ② [i] - cnt 지금 까지 출력한 횟수
# for i in range(length - 1, -1, -1):
# for (int i = len - 1; i >= 0; i--) {
#     if (cnt >= a) break;
#     printf("%c", str[i]);
#     ++cnt;
# }