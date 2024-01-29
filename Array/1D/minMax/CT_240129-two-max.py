# [n개의 숫자 중 최대 2개 ](https://www.codetree.ai/missions/4/problems/two-max-of-n-num)

# 10 << [0]=max이면, max2nd=[0]로 초기화하면 오답발생
# 2147483647 100 2 3 -400 -2147483648 2 3 0 -1

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

print(max, max2nd)

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