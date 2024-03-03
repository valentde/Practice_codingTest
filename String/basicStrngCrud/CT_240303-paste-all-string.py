# [문자열 전부 붙이기 ](https://www.codetree.ai/missions/4/problems/paste-all-string)
n = int(input())

strList = [ input() for _ in range(n)]

str = ''.join(strList)
print(str)