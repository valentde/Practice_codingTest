# [n개의 숫자 중 최대 2개 ](https://www.codetree.ai/missions/4/problems/two-max-of-n-num)

# ((초기화 [0]오답)) [0]=max → max2nd=[0] → 😡
# 10
# 2100 100 2 3 -400 -2100 2 3 0 -1

### 내림차순 정렬
# int → Integer 배열변환 : Integer[] A2 = Arrays.stream(A).boxed().toArray(Integer[]::new);

# Java : Arrays.sort(A2, Collections.reverseOrder());
# C++ : sort(A, A+n, greater<int>());
# PY : arr.sort(reverse=True)

import sys
n = int(input())
arr = list(map(int, input().split()))

max= -sys.maxsize
index=0
for i in range(len(arr)):
    if(max < arr[i]):
        index= i
        max = arr[i]

max2nd = -sys.maxsize
for i in range(len(arr)):
    if(arr[i]== max):
        if(i == index):
            continue
        else:
            max2nd = max
        
    if(max2nd < arr[i]):
        max2nd = arr[i]
### LOOP 2번 (max1st, max2nd 변수)
# Step 1: max1과 해당 index를 구합니다.
max1, max1_idx = arr[0], 0

for i in range(1, n):
    if arr[i] > max1:
        max1, max1_idx = arr[i], i  # 최대 위치를 갱신합니다.

# Step 2: max1이 골라진 위치를 제외한 곳에서 최댓값을 구합니다.
is_initialized = False
for i in range(n):
    if i == max1_idx:
        # Case 1 : 1번에서 고른 케이스는 패스합니다.
        continue

    if not is_initialized:
        # Case 2: 아직 max2 값을 초기화 하지 못했다면
        #         현재 값으로 초기화 합니다.
        is_initialized, max2 = True, arr[i]
    elif arr[i] > max2:
        # Case 3: 지금까지 계산한 값보다 좋다면 갱신합니다.
        max2 = arr[i]

### LOOP 1번 (max1st, max2nd 변수)
# Step 1) 처음 2개의 원소 중 더 큰 값을 max1에
#                        더 작은 값을 max2에 넣습니다.
# Step 2) i 〉= 2 에 해당하는 남은 원소들을 순서대로 보면서 다음 규칙에 따라 maxl, max2를 갱신해줍니다.
#     case 1) [i] >= max         이면 : max2nd = max , max=[i]
#     case 2) max > [i] > max2nd 이면 : max2nd = [i]
if arr[0] > arr[1]:
    max1, max2 = arr[0], arr[1]
else:
    max2, max1 = arr[0], arr[1]

for i in range(2, n):
    if arr[i] >= max1:
        max2, max1 = max1, arr[i]
    elif arr[i] > max2:
        max2 = arr[i]

print(max1, max2)

# [2가 3번째로 등장하는 위치 ](https://www.codetree.ai/missions/4/problems/where-2-appears-3rd)
n = int(input())
arr = list(map(int, input().split()))

index, cnt2 = 0, 0
for i in range(n):
    if arr[i] == 2:
        cnt2 += 1
        if(cnt2 == 3):
            index = i
            break
print(index + 1)