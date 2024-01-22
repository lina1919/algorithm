import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
  #print(stack)
  str = input().rstrip()
  #print(str)
  if str == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])
  elif str == 'size':
    print(len(stack))
  elif str == 'pop':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack.pop())
  elif str == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  else:
    #print(str)
    s,num = str.split( )
    if s == 'push':
      stack.append(int(num))
