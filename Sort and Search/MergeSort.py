def MergeSort(a,p,q,r):
    n1=q-p
    n2=r-q-1
    L=list(0 for i in range(0,n1))
    R=list(0 for i in range(0,n2))
    for i in range(n1):
        L[i]=a[p+i]
    for i in range(n2):
        R[i]=a[q+i+1]
    i=0
    j=0
    for k in range(p,r):
        if L[i]<=R[j]:
            a[k] = L[i]
            i+=1
        elif a[k]==R[j]:
            j+=1
    return a

N=int(input())
a=list(0 for i in range(0,N))
for i in range(N):
    a[i]=int(input())
    
print(MergeSort(a,0,N//2,N))