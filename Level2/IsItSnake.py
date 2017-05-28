def answer(row1, row2):
    columns=len(row1)
    snakeFound=0
    stray=0
    snakeFoundColumn=0
    for i in range(columns-1):
        if row1[i]=='#':
            if row1[i+1]=='#' and row2[i]=='#':
                stray+=1
                snakeFound=1
                continue
            if row2[i]=='#':
                snakeFound=1
                continue
            elif row1[i+1]=='#':
                snakeFound=1
                continue
            else:
                if i==0:
                    return 'no'
                elif row1[i-1]!='#':
                    return 'no'
                else:
                    continue
        elif row2[i]=='#':
            if row2[i+1]=='#' and row1[i]=='#':
                stray+=1
                snakeFound=1
                continue
            if row1[i]=='#':
                snakeFound=1
                continue
            elif row2[i+1]=='#':
                snakeFound=1
                continue
            else:
                if i==0:
                    return 'no'
                elif row2[i-1]!='#':
                    return 'no'
                else:
                    continue
    if snakeFound==1:
        return 'yes'
    return 'no'

testcases=int(input())
for i in range(testcases):
    num=int(input())
    row1=input()
    row2=input()
    print(answer(row1, row2))

            
