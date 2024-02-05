# [특정 원소들의 합 ](https://www.codetree.ai/missions/4/problems/sum-of-specific-elements)
matrix = [list(map(int, input().split())) for _ in range(4)]

sum=0
for i in range(4):
    # for j in range(i, 4):
    for j in range(0, i + 1):
        sum += matrix[i][j]

print(sum)