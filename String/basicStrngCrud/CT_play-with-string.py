# [문자열 놀이 ](https://www.codetree.ai/missions/4/problems/play-with-string)
# 1 : a번째 문자와 b번째 문자를 교환
# 2 : 문자 a를 전부 문자 b로 변경 (대치)
s, qn = input().split()
ls = list(s)

num = int(qn)
while num >0:
    num -=1
    q = input().split()
    if q[0] == '1':
        a, b = int(q[1]), int(q[2])

        # 1) 내장함수
        tmp = string[a - 1]
        string = string[:a - 1] + string[b - 1] + string[a:]
        string = string[:b - 1] + tmp + string[b:]

        # 2) 글자배열로 분할
        one, two = ls[a-1], ls[b-1]
        ls[a -1] = two
        ls[b -1] = one
        s = ''.join(ls)

        print(s)
    else:
        a, b = q[1],q[2]

        # 문자 a를 전부 b로 변
        for i in range(len(str)):
            if str[i] == a:
                str = str[:i] + b + str[i + 1:]


        ls = list(s)
        for i in range(len(ls)):
            if ls[i] == a:
                ls[i] = b 
        s = ''.join(ls)
        print(s)