# [특정 문자로 끝나는 문자열 ](https://www.codetree.ai/missions/4/problems/string-ending-with-specific-character)
strEnter = [input() for _ in range(10)]
chEnd = input()

condition = False
for w in strEnter:
    if chEnd == w[-1]:
        condition = True
        print(w)
if condition == False:
    print('None')