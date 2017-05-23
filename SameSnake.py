def isSameSnake(snake1Start,snake1End,snake2Start, snake2End):
    #all the formal parameters are simply tuples corresponding to the coordinates for the start and end of snakes
    
    #if both snakes are not parallel the only way in which they are the same snake is if one of the endpoints match with the other snake

    if snake1Start[0]==snake1End[0]:
        # it means snake1 is vertical
        if snake2Start[0]==snake2End[0]:
            # print('both vertical')
            # it means both snakes are vertical
            # in this case for them to be the same snake it has to be on the same line
            if snake1Start[0]==snake2Start[0]:
                return isSnakesOverlapping(snake1Start,snake1End,snake2Start, snake2End, 'vertical')

            else:
                # not in the same line
                return 0

        else:
            # print('first snake vertical, second snake horizontal')
            # not parallel
            # the first snake is vertical and second snake is horizontal
            if snake1Start==snake2Start or snake1Start==snake2End or snake1End==snake2Start or snake1End==snake2End:
                # same snake
                return 1
            else:
                return 0

    else:
        # the first snake is horizontal
        if snake2Start[1]==snake2End[1]: 
            # print('both snakes horizontal')
            # it means that both snakes are horizontal
            # in this case for them to be the same snake it has to be on the same line
            if snake1Start[1]==snake2Start[1]:
                return isSnakesOverlapping(snake1Start,snake1End,snake2Start, snake2End, 'horizontal')
                
            else:
                # not in the same line
                return 0
        else:
            # print('first snake horizontal, second snake vertical')
            # not parallel
            # it means first snake is horizontal and snake 2 is vertical
            if snake1Start==snake2Start or snake1Start==snake2End or snake1End==snake2Start or snake1End==snake2End:
                # same snake
                return 1
            else:
                return 0
            

def isSnakesOverlapping(snake1Start,snake1End,snake2Start, snake2End, alignment):
    # returns true if both snakes are overlapping or not
    if alignment=='vertical':
        # it means x-axis is fixed and y-axis moves
        movingIndex=1
    else:
        # it means y-axis is fixed and x-axis moves
        movingIndex=0
    
    #2 1 8 1, 11 1 9 1
    # print('snake1Start: '+str(snake1Start)+'\nsnake1End: '+str(snake1End)+'\nsnake2Start: '+str(snake2Start)+'\nsnake2End: '+str(snake2End)) #DEBUG
    # print('movingIndex: '+str(movingIndex))

    if snake1Start[movingIndex] < snake2Start[movingIndex]:
        # print('snake 1 < snake 2')
        if (snake1End[movingIndex]<snake2Start[movingIndex]) and (snake1End[movingIndex]< snake2End[movingIndex]):
            # print('snake 1 and snake 2 not overlapping')
            # it means they are not overlapping
            return 0
        else:
            return 1
    else:
        
        if (snake2End[movingIndex]<snake1Start[movingIndex]) and (snake2End[movingIndex]< snake1End[movingIndex]):
            # they are not overlapping
            return 0
        else:
            return 1

testCase=int(input())
# answers=[]
for i in range(testCase):
    snake=input()
    snakeCoordinates=snake.split(' ')
    snake1Start=(int(snakeCoordinates[0]), int(snakeCoordinates[1]))
    snake1End=(int(snakeCoordinates[2]), int(snakeCoordinates[3]))
    snake=input()
    snakeCoordinates=snake.split(' ')
    snake2Start=(int(snakeCoordinates[0]), int(snakeCoordinates[1]))
    snake2End=(int(snakeCoordinates[2]), int(snakeCoordinates[3]))
    if isSameSnake(snake1Start,snake1End,snake2Start, snake2End)==1:
        # answers.append('yes')
        print('yes')
    else:
        # answers.append('no')
        print('no')
# for i in range(testCase):
#     print(answers[i])
