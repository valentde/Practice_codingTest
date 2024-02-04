# [배열의 평균 ](https://www.codetree.ai/missions/4/problems/ave-of-array)
mat = [list(map(int, input().split())) for _ in range(2)]

print(f'{sum(mat[0])/4:.1f} {sum(mat[1])/4:.1f}')

colSum = [0, 0, 0, 0]
for c in range(4):
    colSum[c] = mat[0][c] + mat[1][c]
for cs in colSum:
    print('{0:.1f} '.format( cs /2), end='')


print('\n%.1f' % (sum(colSum) / 8))

# [배열의 합 ](https://www.codetree.ai/missions/4/problems/sum-of-array)
for _ in range(4):
    print(sum(list(map(int, input().split()))))