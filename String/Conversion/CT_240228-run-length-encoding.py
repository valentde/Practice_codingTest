# 틀린이유
#   숫자 → 자릿수 배열 만들기
# 자릿수 배열을 "" 문자열 대신 list()로 만드려고 했음

# [Run Length 인코딩 ](https://www.codetree.ai/missions/4/problems/run-length-encoding)

# Run Length Encoding = 간단한 비손실 압축 방식으로, 연속해서 나온 문자와 연속해서 나온 개수
A = input()
leng, encoding = len(A), list()

# for i in range(leng):
i, ansLen = 0, 0
# for _ in range(leng):
while(i<leng):
    count = 1
    while (i + 1 < leng and A[i] == A[i + 1]):
        i += 1
        count += 1
    encoding.append(A[i])
    encoding.append(count)

    # while(count > 0):
    #     ansLen += 1
    #     count //= 10

    ansLen += 1 + len( list(map(int, str(count))) )

    i += 1

print(ansLen)
for e in encoding:
    print(e, end='')