import sys
input = sys.stdin.readline
n = int(input())
assignments = []
result = 0
for _ in range(n):
  assignment_info = list(map(int, input().split()))
  if assignment_info[0] == 1:
    assignments.append((assignment_info[1], assignment_info[2]))
  if assignments:
    score, time = assignments.pop()
    time -= 1
    if time == 0:
      result += score
    else:
      assignments.append((score,time))
print(result)
