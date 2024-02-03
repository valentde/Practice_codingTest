# [자동차 단일 거래 이익 최대화하기 ](https://www.codetree.ai/missions/4/problems/max-profit-of-single-car)
#  right - left 값 차이 최대
# (1) 완전탐색 O(n^2), O(N)
year = int(input())
price = list(map(int, input().split()))

maxProfit =0
for i in range(year-1):
    for j in range(i+1, year):
        profit = price[j] - price[i]
        if profit >0:
            maxProfit = maxProfit if maxProfit > profit else profit

print(maxProfit)

# (2) Observation ????
# TODO

# [500 근처의 수 ](https://www.codetree.ai/missions/4/problems/near-500)
arr = list(map(int, input().split()))
maxUnder, minOver = 0, 1001

for e in arr:
    if(e < 500):
        maxUnder =  e if e>maxUnder else maxUnder
    elif(e > 500):
        minOver = e if e<minOver else minOver

print(maxUnder, minOver)

