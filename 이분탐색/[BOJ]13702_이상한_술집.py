import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]

start = 1
end = max(arr)

res = 0
while(start<=end):
    mid = (start+end)//2
    count = 0

    count = sum(i//mid for i in arr)

    #count가 많으니까 mid 가 커져도 됨. > start를 크게 
    if count >= k:
        res = mid 
        start = mid+1
    else: # count가 적으면 mid가 작아져야함. > end를 작게
        end = mid-1

print(res)
