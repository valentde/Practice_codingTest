# ct2 시뮬1 | 4-1 날짜와시간 01-04 직접/내장함수/포맷형식
# -01: ✔️0시0분, 1월 1일부터 차이계산 ✖️ 날짜간의차이만
# -02: 날짜차이 : 직접하는거보다 1/1부터 며칠인지
# -03: 시간계산 : minute 단위
# -04: baseWeek[0], 날짜차이음수 while +=7
#
#
# <두 날짜간의 차이가 몇 일인지
# <날짜 차이 계산 방법
# < 날짜차이(같은연도 → 윤년포함 → 다른연도) →→ 요일weekday  →→ 시간차이>
# 1. 내장함수 (권장)
# 2. 직접 계산
# 3. 포맷형식

# int days[13] = {}
# days끼리 빼고나서 +1
#  변수명 -  "각 달에 있는 일수" : days → daysInMonth, monthDays

# [Time to Time ](https://www.codetree.ai/missions/5/problems/time-to-time)
a, b, c, d = list(map(int, input().split()))
print(c*60+d - (a*60+b))

# [Date to Date](https://www.codetree.ai/missions/5/problems/date-to-date/description)
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1, d1, m2, d2 = list(map(int, input().split()))

m1ToDay, m2ToDay = 0,0
for i in range(1, m1):
    m1ToDay += month[i]
for i in range(1, m2):
    m2ToDay += month[i]
print(m2ToDay + d2 -m1ToDay - d1 + 1)

# [DateTime to DateTime ](https://www.codetree.ai/missions/5/problems/datetime-to-datetime)
a, b, c = list(map(int, input().split()))

aToMin, bToMin = a*24*60, b*60
startMin = 11 + 11*60 + 11*60*24

print(aToMin+bToMin+c - startMin)

# [요일맞추기](https://www.codetree.ai/missions/5/problems/guess-day-of-week/description)
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1, d1, m2, d2 = list(map(int, input().split()))
m1ToDay, m2ToDay = 0,0
for i in range(1, m1):
    m1ToDay += month[i]
for i in range(1, m2):
    m2ToDay += month[i]
dayMod = (m2ToDay + d2 -m1ToDay - d1) % 7

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']
print(day[ dayMod ])