import sys

# [모이자 ](https://www.codetree.ai/missions/5/problems/gather)
# ValueError: invalid literal for int() with base 10: '' dp 공백단위 입력 에러 .split(' ') 넣지말고 그냥 .split()
n = int(input())
# arr1 = [0] + list(map(int, input().split(' ')))
arr1 = [0] + list(map(int, input().split()))
sumMin=sys.maxsize
for home in range(1, n+1):
    sum =0
    for i in range(1, n+1):
        sum += arr1[i] * abs(home - i)
    sumMin = min(sumMin, sum)
print(sumMin)

# [이상한 진수 2 ](https://www.codetree.ai/missions/5/problems/awkward-digits-2)
max6= 0
binArr = list(input())
for i, val in enumerate (binArr):
    forArr = binArr[:]
    forArr[i] = '1' if val == '0' else '0'
    dex = int(''.join(forArr), 2)
    max6 = max(max6, dex)
print(max6)

# [원 모양으로 되어있는 방 ](https://www.codetree.ai/missions/5/problems/a-room-in-a-circle)
# 한 쪽 방향 이동 음수일 경우 if 대신 (... +n) % n
N8 = int(input())
arr8 = [int(input()) for _ in range(N8)]
ansMinSum, people = sys.maxsize, sum(arr8)
for start in range(N8):
    sum=0
    for i in range(N8):
        dist  = (i-start)
        if dist <0 :
            dist = dist + N8
        sum += arr8[i] * dist
    ansMinSum = min(ansMinSum, sum)
print(ansMinSum)

