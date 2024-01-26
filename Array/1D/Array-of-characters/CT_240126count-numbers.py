## 3항방정식 + 문자(자음)배열 for-in
# [특정 위치의 문자 ](https://www.codetree.ai/missions/4/problems/char-in-specific-location)
word = ['L', 'E', 'B', 'R', 'O', 'S']

c = input()
print(word.index(c) if c in word else 'None')

# [개수 세기 .count() ](https://www.codetree.ai/missions/4/problems/count-numbers)
n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

print(arr.count(m))