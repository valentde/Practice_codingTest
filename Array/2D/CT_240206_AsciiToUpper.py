# [대문자로 바꾸기 ](https://www.codetree.ai/missions/4/problems/change-to-capital)
for _ in range(5):
    a = list(input().split())
    for e in a:
        # print(e.upper(), end=' ')
        print( chr(ord(e) + ord('A') - ord('a') ), end=' ')
    print()