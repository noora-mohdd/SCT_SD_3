#sudoku solver program

def load_puzzle(file_path):  #load the puzzle from the txt file
    grid=[]
    with open(file_path, "r") as f:
        for line in f:
            grid.append([int(num) for num in line.strip().split()])
    return grid
    
def print_puzzle(grid): #prints the grid
    for row in grid:
        print(" ".join(str(num) if num!=0 else "." for num in row))

def find_empty(grid): #finds the location of the empty cell
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                return i,j
    return None


def is_valid(grid,row,col,num):
    if num in grid[row]: #checks row
        return False
    
    if num in [grid[i][col] for i in range(9)]: #checks column
        return False
    
    box_x=col//3
    box_y=row//3  #figures out which 3X3 box

    for i in range(box_y*3, box_y*3+3): #checks in that box
        for j in range(box_x*3, box_x*3+3):
            if grid[i][j]==num:
                return False
            
    return True #passed all checks

    
def solve(grid):
    empty=find_empty(grid)
    if not empty:
        return True  #puzzle solved
    
    row,col=empty

    for num in range(1,10):
        if is_valid(grid,row,col,num):
            grid[row][col]=num

            if solve(grid):
                return True
            
            grid[row][col]=0 #backtrack
    
    return False

def main():
    file="puzzle.txt"
    sudoku_grid=load_puzzle(file)

    print()
    print("unsolved sudoku: ")
    print_puzzle(sudoku_grid)

    if solve(sudoku_grid):
        print()
        print("Solved Sudoku:")
        print_puzzle(sudoku_grid)
    else:
        print("No solution exists.")
    
if __name__=="__main__":
    main()
