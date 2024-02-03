# [가장 왼쪽에 있는 최댓값 ](https://www.codetree.ai/missions/4/problems/leftmost-max-value)

## 간과함 : 초기max [0] 이므로 탐색은 i=1~maxIndex 탐색:
# (1)
# TODO (2) Observation
n = int(input())
arr = list(map(int, input().split()))

ansList = list()
maxIndex = len(arr) - 1
while maxIndex >0:
    maxIndex = arr.index(max(arr))
    ansList.append(maxIndex)
    arr = arr[:maxIndex:]

for e in ansList:
    print(e + 1, end=' ')