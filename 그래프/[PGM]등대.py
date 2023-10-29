global graph
global light
global count

count = 0

def dfs(current,parent):
    global count
    for next in graph[current]:
        if next == parent:
            continue
            
        dfs(next,current)
        #등대 3개가 있으면 무조건 가운데 등대가 켜져야함
        # 따라서 dfs 시 parent node 까지 같이 넘겨줌
        if light[next] == False and light[current] == False:
            light[current] = True
            count += 1

def solution(n, lighthouse):
    answer = 0
    global graph
    graph = [[] for i in range(n+1)]
    global light
    light = [False for i in range(n+1)]
    
    for left, right in lighthouse:
        graph[left].append(right)
        graph[right].append(left)

    dfs(1,1)
    return count
