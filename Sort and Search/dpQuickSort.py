def dp_quick_sort(A,low,high):
    if low < high:
        lp, rp = partitonDP(A,low,high) #좌우 피벗의 인덱스를 반환받음
        dp_quick_sort(A,low,lp-1)       #low ~ lp-1 정렬
        dp_quick_sort(A,lp+1,rp-1)      #lp+1 ~ rp-1 정렬
        dp_quick_sort(A,rp+1,high)      #rp+1 ~ high 정렬