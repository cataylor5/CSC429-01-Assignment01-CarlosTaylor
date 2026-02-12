from collections import deque


# grid for problems c and d
## 7 rows (0 through 6) and 6 columns (0 through 5)
## each string in this list represents one row of the grid
## index position in the outer list is the row number
## index position inside each string is the column number
## '.' means open cell that can be traversed
## '#' means blocked cell that cannot be traversed
## 'A' is the starting cell at (6,0)
## 'B' is the goal cell at (3,3)

GRID = [
    ".#####",  ## row 0
    "......",  ## row 1 (entire row traversable)
    ".##.##",  ## row 2 open at (2,0) and (2,3)
    ".##B##",  ## row 3 open at (3,0) and goal at (3,3)
    ".#..##",  ## row 4 open at (4,0), (4,2), (4,3)
    ".#.###",  ## row 5 open at (5,0), (5,2)
    "A..###",  ## row 6 open at (6,0), (6,1), (6,2)
]


def find_cell(grid, target):
    ## loops through the grid to find the coordinates of target ('A' or 'B')
    ## grid[r][c] means: row r, column c
    ## once the target character is found, return the coordinate as (row, col)

    for r in range(len(grid)):  ## range(len(grid)) gives row numbers 0 through 6
        for c in range(
            len(grid[0])
        ):  ## range(len(grid[0])) gives column numbers 0 through 5
            if grid[r][c] == target:  ## checks if current cell equals target
                return (r, c)  ## return coordinate tuple


def get_neighbors(grid, r, c):
    ## determines which surrounding cells can be moved to from (r,c)
    ## movement allowed: up, down, left, right
    ## this replaces adjacency list logic used in graph version

    ## moves is a list of row/column changes
    ## (-1,0) means move up one row
    ## (1,0) means move down one row
    ## (0,-1) means move left one column
    ## (0,1) means move right one column
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    neighbors = []  ## empty list to store valid neighbor coordinates

    for dr, dc in moves:  ## dr = change in row, dc = change in column

        nr = r + dr  ## calculate new row position
        nc = c + dc  ## calculate new column position

        ## ensure new coordinate is inside grid boundaries
        ## prevents index error from going outside grid
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):

            ## ensure cell is not blocked
            if grid[nr][nc] != "#":
                neighbors.append((nr, nc))  ## add valid neighbor coordinate

    return neighbors  ## return list of valid neighbor cells


def bfs_grid_path(grid):
    ## locate start and goal coordinates using helper function
    start = find_cell(grid, "A")
    goal = find_cell(grid, "B")

    ## frontier is a queue (FIFO behavior)
    ## deque is used for efficient removal from the front
    frontier = deque([start])

    ## parent dictionary stores which coordinate we came from
    ## allows us to reconstruct path once goal is found
    parent = {start: None}

    ## explored set prevents revisiting cells
    ## start is marked explored immediately
    explored = {start}

    ## continue while there are cells to explore
    while frontier:

        ## remove and return first element from queue
        current = frontier.popleft()

        ## if current cell equals goal coordinate
        if current == goal:

            ## reconstruct pathtaken by walking backward
            pathtaken = []
            node = goal

            ## follow parent links until None (start)
            while node is not None:
                pathtaken.append(node)
                node = parent[node]

            ## reverse because we built path backward
            pathtaken.reverse()
            return pathtaken

        ## unpack coordinate tuple
        r, c = current

        ## explore neighbors of current cell
        for neighbor in get_neighbors(grid, r, c):

            ## only process if not already explored
            if neighbor not in explored:

                explored.add(neighbor)  ## mark as explored immediately

                parent[neighbor] = current  ## record where we came from

                frontier.append(neighbor)  ## add neighbor to queue

    ## if loop ends without reaching goal
    return []


def dfs_grid_path(grid):
    ## locate start and goal coordinates
    start = find_cell(grid, "A")
    goal = find_cell(grid, "B")

    ## frontier is a stack (LIFO behavior)
    ## normal Python list is used for stack behavior
    frontier = [start]

    parent = {start: None}
    explored = {start}

    ## continue while stack is not empty
    while frontier:

        ## remove and return last element from stack
        current = frontier.pop()

        ## if current equals goal coordinate
        if current == goal:

            pathtaken = []
            node = goal

            while node is not None:
                pathtaken.append(node)
                node = parent[node]

            pathtaken.reverse()
            return pathtaken

        r, c = current

        ## retrieve neighbors
        neighbors = get_neighbors(grid, r, c)

        ## reversed is used because stack pops last added first
        ## this preserves directional consistency
        for neighbor in reversed(neighbors):

            if neighbor not in explored:

                explored.add(neighbor)

                parent[neighbor] = current

                frontier.append(neighbor)

    return []


def main():

    ## Problem 1(c): BFS from A to B in grid
    bfs_result = bfs_grid_path(GRID)
    print("BFS path from A to B:", bfs_result)
    print("BFS path length (moves):", len(bfs_result) - 1)

    print()

    ## Problem 1(d): DFS from A to B in grid
    dfs_result = dfs_grid_path(GRID)
    print("DFS path from A to B:", dfs_result)
    print("DFS path length (moves):", len(dfs_result) - 1)


## standard Python entry point
## ensures main() only runs when file executed directly
if __name__ == "__main__":
    main()
