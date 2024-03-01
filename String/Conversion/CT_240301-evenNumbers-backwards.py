# [짝수 번째만 거꾸로 출력 ](https://www.codetree.ai/missions/4/problems/print-only-even-numbers-backwards)

# 내풀이 : 짝수 배열 추출 → 거꾸로
# 모범 : lastEvenIndex 구해서 2칸씩 앞으로

# 마지막 index 값 짝수  = 마지막 글자가 홀수 번째

s = input()

evenStr = s[1::2]
print(evenStr[::-1])