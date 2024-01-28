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