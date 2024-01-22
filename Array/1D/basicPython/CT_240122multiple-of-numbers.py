# [숫자들의 배수](https://www.codetree.ai/missions/4/problems/multiple-of-numbers)
cntBreak=0
n = int(input())

mul = 1
while cntBreak< 2:
    print(n * mul, end=' ')
    cntBreak += 1 if (n * mul)%5==0 else 0
    mul += 1

# [ 배수 저장] mul 대신 +arr[0]
arr = []
for i in range(1, 10):
    a = arr[i - 1] + arr[0]
	arr.append(a)

# [특정 조건에 맞게 출력하기 ](https://www.codetree.ai/missions/4/problems/print-in-specific-conditions)
## 특정 값 전까지 출력
arr = list(map(int, input().split()))

for e in arr:
    if(e ==0):
        break
    print( (e//2) if e%2==0 else e+3, end=' ')