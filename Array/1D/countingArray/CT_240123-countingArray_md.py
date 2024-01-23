# (PY) 10곱하는 출력형식 - f"{i}0" 가능..!

# Count 배열 / 1-9 개수 세기
# - 배열값 들이 한정 + 여러번 등장
# - 각 숫자가 몇 번 나왔는지
# - 각각의 빈도를 저장
# ① 2중반복문  : for 빈도 for 검색대상배열
# ② 단순반복 :    for 검색대상배열  빈도[ 배열값 ]++
# 	       for 검색대상배열  빈도[ 배열값 ] += 1


## 배열 초기화(2) [ deafult값으로 전체 초기화 ]
# ( C )
# // 숫자 별 출현 횟수.       1  2  3  4  5  6
# int count_arr[7] = { 0, 0, 0, 0, 0, 0, 0 };
# int count_arr[7] = { 0, };
#
# ( C++ )
# // 숫자 별 출현 횟수.       1  2  3  4  5  6
# int count_arr[7] = { 0, 0, 0, 0, 0, 0, 0 };
# int count_arr[7] = {};
#
# (JAVA)
# // 숫자 별 출현 횟수.              1  2  3  4  5  6
# int[] countArr = new int[]{ 0, 0, 0, 0, 0, 0, 0 };
# int[] countArr = new int[7];
#
# [ PYTHON]
# count_arr = [0, 0, 0, 0, 0, 0, 0]
# count_arr = [0] * 7
# count_arr = [0 for _ in range(7)] # list comprehension
#
# (JS)
# // 숫자 별 출현 횟수.   1  2  3  4  5  6
# let countArr = [ 0, 0, 0, 0, 0, 0, 0 ];
# let countArr = Array(7).fill(0);  #fill(값) 함수

# [점수대 파악하기 ](https://www.codetree.ai/missions/4/problems/find-out-the-score-range)
arr = list(map(int, input().split()))

count10Unit = [0]*11

for e in arr:
    if e==0:
        break
    count10Unit[ e//10 ] +=1

for i in range(10, 0, -1):
    # print('%d - %d' % (i*10, count10Unit[i]))
    print(f"{i}0 - {count10Unit[i]}")