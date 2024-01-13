
# https://www.codetree.ai/missions/4/problems/credit-calculator/introduction
n = int(input())
grades = list(map(float, input().split()))

sum=sum(grades)
avg = sum / len(grades)

print('{0:.1f}'.format(avg))
print('Perfect' if avg>=4.0 else 'Good' if avg>=3.0 else 'Poor')