# [출력결과 11 ](https://www.codetree.ai/missions/4/problems/reading-k201531)
### ( 2차원 배열 ) 선언+ 다른값 초기화
# int arr[3][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} }; #C/C++
# int[][] arr = new int[][]{ {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
# let arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

for i in range(3):
    for j in range(3):
        print("ANSWER", end = ' ')
    print()


# 출력결과
# 7 4 1
# 8 5 2
# 9 6 3


# 발전과정
# 123     147     741
# 456     258     852
# 789     369     963