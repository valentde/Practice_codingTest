
# min(원소2개뺄셈)                = O(N^2)
# min(원소2개뺄셈) + Ascending배열 = O(N) (붙어있는 원소뺄셈 중 최솟값)

# [두 숫자의 차의 최솟값 ](https://www.codetree.ai/missions/4/problems/minimum-difference-between-two-numbers)
n = int(input())
naturals = list(map(int, input().split()))

# 절대값 |뺄셈| 가장 작음
gap = 100
for i in range(n):
    for j in range(i+1, n):
        localGap = abs(naturals[i] - naturals[j])
        gap = gap if gap<localGap else localGap

print(gap)