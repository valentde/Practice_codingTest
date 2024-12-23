# [구간 중 최대 합 ](https://www.codetree.ai/missions/5/problems/max-sum-of-subarray)
# 구간크기 입력값으로 고정(k1)
# 구간단위 완탐 → 시작지점 기준 진행
# n-k 인지 n-k-1인지 헷갈린다면
n1, k1 = map(int, input().split(' '))
arr1 = list(map(int, input().split()))
sum1, sumLocal1 = [0] * 2

for i in range(n1 - k1 + 1):
    sumLocal1 = 0
    for j in range(i, i + k1):
        sumLocal1 += arr1[j]
    sum1 = max(sumLocal1, sum1)
print(sum1)

# [G or H 3 ](https://www.codetree.ai/missions/5/problems/G-or-H-3)
# 배열생성 : rangeMax 대신 → inputMax 기준
# (함정) 1크기(K)란 양쪽 끝에 있는 x값 끼리의 차 || 끝시작 1번지~inputMax
# (함정) inputMax기준 배열생성하면 탐색범위가 더 큰 예외 경우 처리
# 해설은 for문 , 내답은 slicing
n2, k2 = map(int, input().split(' '))
points = []
for _ in range(n2) :
    x, y = input().split(' ')
    x = int(x)
    y = 1 if y == 'G' else 2
    points.append([x, y])
points.sort(key=lambda x: - x[0])
biggestN = points[0][0]
arr2 = [0] * (biggestN + 1)

for pos, val in points:
    arr2[pos] += val

# 끝시작 1번지-k개
sum2=0
# for i in range(n + 1 - k2):
for i in range(biggestN - k2 + 1):
# for i in range(biggestN - k2 + 2):
#     sum2 = max( sum( arr2[i:i + k2] ) , sum2)
    sum2 = max( sum( arr2[i:i + k2 + 1] ) , sum2)
# 예외 케이스
if k2 > biggestN:
    sum2 = sum(arr2)
print(sum2)