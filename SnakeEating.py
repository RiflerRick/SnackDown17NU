def answer(l, k):
    # lengthList is a list of lengths of all the snakes
    lengthList=l[:]
    num=0
 
    # sorting the list in ascending order 
    lengthList.sort()
    index=len(lengthList)-1
    while index>0:
        # traversing the list from back to front
        if int(lengthList[index])>=k:
            num+=1
 
            # pop the length of the snake that is already going to be greater than k
            index-=1
        
        else:
            lengthList[index]=str(int(lengthList[index]+1))
            lengthList.pop(index-1)
            index-=1
 
    # here we will land at index=0
    if int(lengthList[index])==k:
        num+=1
 
    return num
 
testcase=int(input())
for i in range(testcase):
    firstLine=input() # this line o
    firstLineList=firstLine.split(' ')
    numSnakes=int(firstLineList[0]) 
    numQueries=int(firstLineList[1])
    snakeLengthString=input()
    snakeLengthList=snakeLengthString.split(' ')
    # snakeLengthList = list(map(int, snakeLengthString.split(' ')))
    # map function is used to map characters to integers in one go
    for j in range(numQueries):
        query=input()
        query=int(query)
        # print('list now:'+str(snakeLengthList))
        print(answer(snakeLengthList, query)) 