# 칭호의 개수가 10^5개, 캐릭터의 개수가 10^5개 이기 때문에 단순 반복문으로는 안됨
# 이분탐색을 해야함
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
chingho = [input().split() for _ in range(n)]
chingho.sort(key=lambda x: int(x[1]))  # 오름차순 정렬

chars = [int(sys.stdin.readline().strip()) for _ in range(m)]

for char in chars:
    right = len(chingho)
    left = 0
    result = 0
    while left <= right:
        mid = (left+right)//2
        if int(chingho[mid][1]) >= char:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    print(chingho[result][0])
