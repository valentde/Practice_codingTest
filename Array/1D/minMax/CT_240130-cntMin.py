# min값 등장횟수 - loop 1번
n = int(input())
arr = list(map(int, input().split()))

cntMin, valMin =0, arr[0]

for e in arr:
    if(valMin > e):
        valMin = e
        cntMin =1
    elif(valMin == e):
        cntMin += 1   

print(valMin, cntMin)