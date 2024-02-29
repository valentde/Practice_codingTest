#    Python 출력할땐 (+= 안되지만, 문자열 연산 에서는 가능
#    num_str = num_str[1:] + num_str[0]

# [합을 옆으로 밀어 출력 ](https://www.codetree.ai/missions/4/problems/push-the-sum-sideways-to-output)
n = int(input())
sum =0
for _ in range(n):
    sum += int(input())

numStr = str(sum)
print('{0}{1}'.format(numStr[1::], numStr[0]))

