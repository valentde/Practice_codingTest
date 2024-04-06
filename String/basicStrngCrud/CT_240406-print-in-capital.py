# [대문자로 출력하기 ](https://www.codetree.ai/missions/4/problems/print-in-capital)
s = input()

result= ''
for e in s:
    if e.isalpha():
        result += e.upper()
print(result)

# [소문자와 숫자 ](https://www.codetree.ai/missions/4/problems/letter-and-number)
s = input().lower()
for e in s:
    if e.isdigit() or e.isalpha():
        print(e, end='')

