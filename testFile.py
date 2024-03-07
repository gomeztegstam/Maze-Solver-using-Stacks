from Stack import Stack
from lab04 import solveMaze
def test_mazewithsolution():
    maze = [
        ['+', '+', '+', '+', 'G', '+'],
        ['+', ' ', '+', ' ', ' ', '+'],
        ['+', ' ', ' ', ' ', '+', '+'],
        ['+', ' ', '+', '+', ' ', '+'],
        ['+', ' ', ' ', ' ', ' ', '+'],
        ['+', '+', '+', '+', '+', '+']
    ]
    assert solveMaze(maze, 4, 4) == True


def test_maze_with_no_solution():
    maze = [['+', '+', '+', '+', 'G', '+'],
            ['+', ' ', '+', ' ', ' ', '+'],
            ['+', ' ', ' ', ' ', '+', '+'],
            ['+', '+', '+', '+', ' ', '+'],
            ['+', ' ', ' ', ' ', ' ', '+'],
            ['+', '+', '+', '+', '+', '+']]
    assert solveMaze(maze, 4, 4) == False
def test_straight_forward_path():
    maze = [[' ', ' ', ' ', ' ', 'G']]  
    assert solveMaze(maze, 0, 0) == True
