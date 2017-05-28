def answer(initialPositions, snakeLength, A, B):
    
    minDistance=0
    stretch=A
    while True:
        if initialPositions==[]:
            break
        small=abs(int(initialPositions[0])-stretch)
        pos=0
        for i in range(len(initialPositions)):
            distance=abs(int(initialPositions[i])-stretch)
            if distance==0:
                pos=i
                break
            if distance<small:
                small=distance
                pos=i
        
        minDistance+=small
        stretch+=snakeLength
        # print('minDistance: '+str(small))
        # print('popped value:'+str(initialPositions[pos]))
        initialPositions.pop(pos)
    
    return minDistance

testcase=int(input())
n, l, a, b = input().strip().split()
n, l, a, b = [int(n), int(l), int(a), int(b)]
pos=input().split(' ')
print(answer(pos, l, a, b))

    
    
