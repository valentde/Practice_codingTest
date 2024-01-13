
# https://www.codetree.ai/missions/4/problems/print-average
a = list(map(float, input().split()))

print(f"{sum(a)/len(a):.1f}")

# https://www.codetree.ai/missions/4/problems/reaching-specific-number
i, sum = 0,0
while(i<10 and arr[i]<250):
    sum += arr[i]
    i += 1

print(sum, f'{sum/(i):.1f}')

# https://www.codetree.ai/missions/4/problems/receive-10-inputs
arr = list(map(int, input().split()))

i, sum = 0,0
while(i<10 and arr[i]>0):
    sum += arr[i]
    i += 1

print(sum, f'{sum/(i):.1f}')
