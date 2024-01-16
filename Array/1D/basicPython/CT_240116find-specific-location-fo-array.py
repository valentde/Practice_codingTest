# https://www.codetree.ai/missions/4/problems/find-specific-location-fo-array
arr = list(map(int, input().split()))
sum2 = sum(arr) - sum(arr[::2])
sum3, avg, cnt = 0, 0.0, 0

for e in arr:
    if e%3==0:
        sum3 += e
        cnt += 1


print(sum2, sum3/cnt)

# https://www.codetree.ai/missions/4/problems/find-specific-location-fo-array-2
arr = list(map(int, input().split()))

odd = sum(arr[::2])
even = sum(arr[1::2])

print(abs(odd-even))


# https://www.codetree.ai/missions/4/problems/find-specific-location-fo-array-3/introduction
arr = list(map(int, input().split()))
i=0
while arr[i] != 0:
    i +=1
print(sum(arr[i-3:i:]))

