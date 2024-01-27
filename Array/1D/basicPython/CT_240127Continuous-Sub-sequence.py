# Continuous Sub-sequence
# [연속부분수열일까 ](https://www.codetree.ai/missions/4/problems/contiguous-array-or-not)

## 어려워던 부분
# A>B배열 포함검사 B인덱스 마지막 검사시작위치 ai - bi
# ex A[7], B[6] 마지막 시작위치는 1

## 더 빠른풀이 :2중 for문(A) isTrue =True 초기화
#                 for문(B)--if a+b>=n1 break -- A[a+b]!=B[b] brea
#             A 반복문 마지막에서 isTrue검증

## (PY) 함수 return 같은역할 import sys --> sys.exit()
## (PY) if in , if not in 할때 is 넣는 실수XX

## (JS) 정수 2개입력 : let [n1, n2] = input[0].split(" ").map(Number);

n1, n2 = tuple(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

isContinuous = False

if B[0] not in A:
    isContinuous = False
else:
    for si in range( A.index(B[0]), n1 - n2 +1 ):
        a = A[si: si+n2]
        i=0
        while i<n2:
            if(a[i] != B[i]):
                 break
            i +=1
        if(i == n2):
            isContinuous = True
            break


print('Yes' if isContinuous else 'No')

# [배열 놀이 ](https://www.codetree.ai/missions/4/problems/play-with-array)
n, query = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

for _ in range (query):
    q = list(map(int, input().split()))

    if q[0]== 1:
        print(arr[ q[1] - 1 ])
    if q[0]== 2:
        if q[1] not in arr:
            print(0)
        else:
            print(arr.index(q[1]) + 1)
    if q[0]== 3:
        new_arr = arr[q[1] -1 : q[2] :1 ]
        for n in new_arr:
            print(n, end=' ')
        print()