import sys
import heapq

input = sys.stdin.readline
n = int(input()) #아이들과 거점지를 방문한 횟수
present = []
for i in range(n): 
  arr = list(map(int, input().split()))
  if arr[0] == 0: #아이들을 만남
    if len(present) == 0:
      print(-1)
    else:
      p = heapq.heappop(present)
      print(p[1])
  else:
    num, presentInfo = arr[0], arr[1:]
    for i in range(num):
      #최대 힙을 만들기 위해 힙에 원소를 추가할때 튜플 형태로 넣어주면 튜플의 첫 번째 원소를 우선순위로 힙을 구성하게 된다는 아이디어를 이용한다.
        heapq.heappush(present, (-presentInfo[i],presentInfo[i]))

#heapq가 더 빠르기 때문에 그걸 쓰는게 더 낫다고 한다
# from queue import PriorityQueue

# n=int(input())
# pq=PriorityQueue()
# for i in range(n):
#     data=list(map(int,input().split()))
#     if data[0]==0:
#         if pq.empty():
#             print(-1)
#         else:
#             print(-pq.get())
#     else:
#         for i in range(1,data[0]+1):
#             pq.put(-data[i])
