def answer(l,k):
    num=0
    j=len(i)
    for i in l:
        if int(i)>=k:
            num+=1
        elif int(i)
    
testCase=int(input())
while testCase>0:
    testCase-=1
    N,Q=input().split(' ')
    L=input().split(' ')
    Q=int(Q)
    while Q>0:
        Q-=1
        k=int(input())
        print(answer(L,k))

    