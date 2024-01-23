### 배열 초기화(1) [앞부분 몇개만 초기화 ]
# int arr[100] = {1, n}; // (C, C++)  {정적배열}
#
# arr = [1, n] 	//(PY) [동적배열]
# let arr = [1, n];	//(JS)
#
# int[] arr = new int[100]; //(JAVA) 동시불가
# arr[0] = 1; arr[1] = n;

### (PY) 처음 두 수  ❌list ⭕tuple
# i = input().split() || a, b = int(i[0]), int(i[1])
v1, v2 = tuple(map(int, input().split()))

# [100 도달하기 ](https://www.codetree.ai/missions/4/problems/reach-100)
n = int(input())
list =  [1, n]

i, sum = 2, 1+n
while sum  < 100 +1:
    sum = list[i-1] + list[i-2]
    list.append(sum)
    i += 1

for l in list:
    print(l, end=' ')

# [전항의 두 배 ](https://www.codetree.ai/missions/4/problems/twice-the-previous)
a, b = tuple(map(int,  input().split()))

arr = [a, b]
for i in range(2, 10):
    arr.append(arr[i-1] + 2*arr[i-2])

for a in arr:
    print(a, end=' ')