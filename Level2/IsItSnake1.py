"""
The way to solve this problem would be to fix paths and figure out a path in which the snake could lie
"""
snakeFound=0

def checkMoreSnakes(row1, row2, index):
    while index<len(row1):
        if row1[index]=='#' or row2[index]=='#':
            # print('found another snake')
            return 0
        index+=1
    return 1

def path(trace, row1, row2, index, snakeFound):
    # print('came from row: '+str(trace))
    # print('current index :'+str(index))

    if trace==0: # denoting it is row1, the snake path starts from row1
        if index==len(row1)-1:
            if row1[index]=='#':
                return 1
            elif row2[index]=='#':
                return 0
            else:
                if snakeFound==1:
                    return 1
                else:
                    return 0
        if row1[index]=='#' and row2[index]=='#':
            # print('going here')
            snakeFound=1
            return path(1, row1, row2, index+1, snakeFound)
        elif row1[index]=='#':
            snakeFound=1
            return path(0, row1, row2, index+1, snakeFound)
        elif row2[index]=='#':
            return 0
        else:
            if snakeFound==1:
                return checkMoreSnakes(row1, row2, index+1)
            else:
                return 0
    elif trace==1:
        if index==len(row1)-1:
            if row2[index]=='#':
                return 1
            elif row1[index]=='#':
                return 0
            else:
                if snakeFound==1:
                    return 1
                else:
                    return 0
        if row2[index]=='#' and row1[index]=='#':
            snakeFound=1
            return path(0, row1, row2, index+1, snakeFound)
        elif row2[index]=='#':
            snakeFound=1
            return path(1, row1, row2, index+1, snakeFound)
        elif row1[index]=='#':
            return 0
        else:
            if snakeFound==1:
                return checkMoreSnakes(row1, row2, index+1)
            else:
                return 0

def answer(row1, row2):
    columns=len(row1)
    ans=''
    for i in range(columns):
        if row1[i]=='#' and row2[i]=='#':
            ans1=path(0, row1, row2, i+1, snakeFound) 
            ans2=path(1, row1, row2, i+1, snakeFound)
            return 'yes' if (ans1 or ans2) else 'no'
        elif row1[i]=='#':
            ans=path(0, row1, row2, i+1, snakeFound)
            return 'yes' if ans else 'no'
        elif row2[i]=='#':
            ans=path(1, row1, row2, i+1, snakeFound)
            return 'yes' if ans else 'no'

    if snakeFound==0:
        return 'no'


testcases=int(input())
for i in range(testcases):
    num=int(input())
    row1=input()
    row2=input()
    snakeFound=0
    print(answer(row1, row2))
