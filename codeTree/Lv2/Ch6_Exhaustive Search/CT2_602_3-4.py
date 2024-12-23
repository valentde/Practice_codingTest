# [특정 구간의 원소 평균값 ](https://www.codetree.ai/missions/5/problems/elemental-mean-value-for-a-particular-interval)
# 부분베열 | 평균 | 부분배열 내 정수 값 포함여부 | 부분배열 vs 부분문자열 함수혼동
# 1) 부분배열 (모든경우) 경계설정 2가지
# 2) 몫x, 몫+나머지X → 소수점까지 출력해야..
# 3) 존재여부 .find() 함수 문자열전용인데 헷갈림
# 심화) Slicing → 생성기 표현식으로 1줄 축소
# cnt = sum(1 for i in range(n) for j in range(n - i) if (_list[i:i + j + 1].count(sum(_list[i:i + j + 1]) / (j + 1)) > 0))

n3 = int(input())
arr3 = list(map(int, input().split(' ')))

# arrStr = ''.join(map(str,arr3))

ans3 = 0
for start in range(n3):
    for j in range(start, n3):
        # for k in range(start, j + 1):
        # avg = sum(arr3[start : j + 1]) // (j+1 - start) + sum(arr3[start : j + 1]) % (j+1 - start)
        avg = sum(arr3[start: j + 1]) / (j + 1 - start)
        if arr3.count(avg) > 0:
            ans3 = ans3 + 1
print(ans3)

# [아름다운 수열 2 ](https://www.codetree.ai/missions/5/problems/beautiful-sequence-2)
# 아름수열은 부분문자열/수열 모든 경우의 수
# 맨처음 입력할때는 sorted()
# 리스트가 같은 내용인지?

N4, M4 = map(int, input().split())
# A4, B4 = input().split(' '), input().split(' ')
# ValueError: invalid literal for int() with base 10: '
# 오류 메시지는 input().split(' ')이 빈 문자열을 반환할 때, int()로 변환을 시도하여 발생한 것으로, 입력 데이터 형식이 예상과 다르거나 불필요한 공백이 있을 수 있음을 나타냅니다.
A4, B4 = input().split(), input().split()
listA4, listB4 = list(map(int, A4)), sorted(list(map(int, B4)))
count4 = 0

if N4 < M4 :
    print(0)
    exit()

# 아름수열(2) B크기만큼 모둔구간 탐색 - 매번정렬
for si in range(N4 - M4 + 1):
    arrMSorted = sorted(listA4[si: si + M4])
    # isSame: bool = True
    # for m in range(M4):
    #     if arrExtract[m] != listB4[m]:
    #         isSame = False
    #         break
    if arrMSorted == listB4:
        count4 += 1
print(count4)