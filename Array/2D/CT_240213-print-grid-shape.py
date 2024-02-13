# [격자 모양 출력하기 ](https://www.codetree.ai/missions/4/problems/print-grid-shape)
n, m = map(int, input().split())
grid = [ [0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    r, c = map(int, input().split())
    grid[r][c] = r * c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(grid[i][j], end=' ')
    print()