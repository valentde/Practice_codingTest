

#  list(input().split()) 와
#       input().split() 만 있는거 차이점?
n = int(input())

str = ''.join(input().split())

for i in range(0, len(str), 5):
    print(str[ i : i+5])


n = int(input())
a = list(input().split())
b = []
s = ''
r = 0
for i in a:
    s += i
for i in range(len(s)):
    if i % 5 == 0 and i != 0:
        print(s[r:i])
        r = i
print(s[r:])

i = 0
while i + 5 <= len(str):
    print(str[i:i+5])
    i += 5
print(str[i:])