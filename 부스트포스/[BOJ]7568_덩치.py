n = int(input())
arr = []
answer = []
for i in range(1,n+1):
    l = list(map(int,input().split()))
    l.append(i)
    arr.append(l)
for i in range(n):
    cnt = 1
    x,y = arr[i][0],arr[i][1]
    for j in range(n):
        if i!=j:
            a,b = arr[j][0],arr[j][1]
            if x<a and y<b:
                cnt += 1
    answer.append(cnt)
print(' '.join(map(str,answer)))

