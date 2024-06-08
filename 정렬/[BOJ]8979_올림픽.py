n,k = map(int,input().split())
arr = []
for _ in range(n):
    l = list(map(int,input().split()))
    arr.append(l)
arr.sort(key=lambda x:(x[1],x[2],x[3]),reverse = True)
for i in range(n):
    arr[i].append(i+1)

for i in range(n-1):
    if arr[i][1] == arr[i+1][1]:
        if arr[i][2] == arr[i+1][2]:
            if arr[i][3] == arr[i+1][3]:
                arr[i+1][4] = arr[i][4]
for a in arr:
    if a[0] == k:
        print(a[4])
