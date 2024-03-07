from Stack import Stack

def solveMaze(maze, startX, startY):
    stack = Stack()
    stack.push([startX, startY])
    stepnum = 1
    maze [startX] [startY] = stepnum
    while stack.isEmpty() == False:
        current_x, current_y = stack.peek()
    
        if (maze[current_x-1][current_y] == ' ') or (maze[current_x-1][current_y] == 'G'):
            if maze[current_x-1][current_y] == 'G':
                return True
            stack.push([current_x-1,current_y])
            stepnum += 1
            maze[current_x-1][current_y] = stepnum 
        elif (maze[current_x][current_y-1] == ' ') or (maze[current_x][current_y-1] == 'G'):
            if maze[current_x][current_y-1] == 'G':
                return True
            stack.push([current_x,current_y-1])
            stepnum += 1
            maze[current_x][current_y-1] = stepnum
        
        elif (maze[current_x+1][current_y] == ' ') or (maze[current_x+1][current_y] == 'G'):
            if maze[current_x+1][current_y] == 'G':
                return True
            stack.push([current_x+1,current_y])
            stepnum += 1
            maze[current_x+1][current_y] = stepnum
        
        elif (maze[current_x][current_y+1] == ' ') or (maze[current_x][current_y+1] == 'G'):
            if maze[current_x][current_y+1] == 'G':
                return True
            stack.push([current_x,current_y+1])
            stepnum += 1
            maze[current_x][current_y+1] = stepnum
        else:
            stack.pop()
            if stack.isEmpty():
                return False
    return False
