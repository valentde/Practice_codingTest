#ct2 시뮬1 | 4-2 radix(진법) 01-04
# -01: to bin
# -02: to decimal
# -03: 10 to 다른진수
# -04: 2 to 10 (x17) to 2
#
#
# 1. Decimal 변환 새 방법🎃
# 2. Decimal To -Radix 5가지 방법
# 3. (py) 숫자리스트 → 문자열 병합 ''join()  오류
# - 문자인자만 가능
# - 변환방법 3가지

# [2진수로 변환하기 ](https://www.codetree.ai/missions/5/problems/convert-to-binary)
n = int(input())
binDigits = []

while n > 0:
    binDigits.append(n % 2)
    n //= 2

for k in range(len(binDigits)-1, -1, -1):
    print(binDigits[k], end='')

# [10진수로 변환하기 ](https://www.codetree.ai/missions/5/problems/convert-to-decimal)
binStr = input()
binStrList = list(binStr)

dec=0
for e in binStrList:
    dec = dec*2 + int(e)

print(dec)

# [여러가지 진수변환 ](https://www.codetree.ai/missions/5/problems/various-numeral-system-transformations)
n, B = map(int, input().split())
radixList = []

while n>0 : 
    radixList.append(n % B)
    n //= B

radixList.reverse()
for e in radixList:
    print(e, end='')

# [십진수와 이진수 2 ](https://www.codetree.ai/missions/5/problems/decimal-and-binary-number-2)
binList = list(input())

dec=0
for i in range(len(binList)):
    dec = dec * 2 + int( binList[i] )

dec *= 17
radixList = []
while dec>0 : 
    radixList.append(dec % 2)
    dec //= 2

radixList.reverse()
for e in radixList:
    print(e, end='')