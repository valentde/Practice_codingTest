# [알파벳 지우기 ](https://www.codetree.ai/missions/4/problems/remove-alphabet)
sum=0
for _ in range(2):
    str = input()
    
    numStr =''
    for e in str:
        if e.isdigit():
            numStr += e
    sum += int(numStr)

print(sum)