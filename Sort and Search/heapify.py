def heapify(arr,n,i):
    largest = i #i번째가 가장 크다고 하자. 
    l = 2*i+1   #왼쪽 자식: left = 2*i+1 (배열 0번을 사용)
    r = 2*i+2   #오른쪽 자식: right = 2*i+2 (배열 0번을 사용)

    if l < n and arr[i] < arr[l]:   #교환조건 검사
        largest = l                 #교환조건 검사
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i :               #교환이 필요하면
        arr[i], arr[largest] = arr[largest],arr[i] #교환
        heapify(arr,n,largest)  #순환적으로 자식노드로 내려감
