# [일의 자리 배열 ](https://www.codetree.ai/missions/4/problems/array-with-units)
i = input().split()
a, b = int(i[0]), int(i[1])

retArr = [a, b]
for _ in range (8):
    c = (a + b)%10
    retArr.append(c)
    a = b
    b = c

for e in retArr:
    print(e, end=' ')

# [제곱하여 출력하기 ](https://www.codetree.ai/missions/4/problems/print-square-of-elements)
n = int(input())
arr = list(map(int, input().split()))

squared = [e**2 for e in arr]

for e in squared:
    print(e, end=' ')

# [짝수인 것만 출력하기 ](https://www.codetree.ai/missions/4/problems/print-even-number)
n = int(input())
arr = list(map(int, input().split()))

evenArr = [e for e in arr if e%2==0]

for e in evenArr:
    print(e, end=' ')