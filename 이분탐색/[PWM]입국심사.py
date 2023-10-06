def solution(n, times):
    low = 0
    #high 값을 times의 가장 작은 값
    high = n * times[0]
    
    mid = (low+high)//2
    
    while high >= low:
        cnt = 0
        #k의 시간 안에 심사가 가능한지 확인
        for i in times:
            cnt += mid//i
            if cnt >= n:
                break
        #심사 가능!
        if cnt >= n:
            high = mid - 1
            mid = (low+high)//2
            
        #심사불가능
        else:
            low = mid + 1
            mid = (low+high)//2
            
    answer = low
    return answer
