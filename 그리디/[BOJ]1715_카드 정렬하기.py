#우선순위 큐 문제
#풀이 참조
#리스트로 sort 사용해서 풀었더니 자꾸 틀렸다고 해서..
import heapq

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

sum = 0
for _ in range(n-1):
    cmp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, cmp)
    sum += cmp
print(sum)


