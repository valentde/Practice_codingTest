# https://www.codetree.ai/missions/4/problems/print-even-numbers-upside-down
n = int(input())
arr = list(map(int, input().split()))
list = []
for e in arr:
    if e %2==0:
        list.append(e)
for e in list[::-1]:
    print(e,end =' ')

    
# https://www.codetree.ai/missions/4/problems/verify-test-passed-2
n = int(input())
ansCnt=0
while n > 0:
    n -= 1
    sumVal = sum(list(map(int, input().split())))
    avg = sumVal / 4.0
    if avg >= 60:
        print('pass')
        ansCnt += 1
    else:
        print('fail')

print(ansCnt)