# Depth-Limited Search (DLS) on the same grid (A start, B goal)

from collections import deque


# grid for problems c and d (same grid used previously)
## 7 rows (0 through 6) and 6 columns (0 through 5)
## '.' means open cell
## '#' means blocked cell
## 'A' is start at (6,0)
## 'B' is goal at (3,3)

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
    ## loops through grid to find target char
    ## returns coordinate tuple (row, col)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == target:
                return (r, c)


def get_neighbors(grid, r, c):
    ## returns valid neighbor coordinates for a given cell (r,c)
    ## movement allowed: up, down, left, right

    ## moves list controls which directions we attempt first
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    neighbors = []

    for dr, dc in moves:
        nr = r + dr
        nc = c + dc

        ## ensure neighbor coordinate stays inside grid
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):

            ## ensure the cell is not blocked
            if grid[nr][nc] != "#":
                neighbors.append((nr, nc))

    return neighbors


def dls_grid_path(grid, limit):
    ## Depth-Limited Search (DLS) is basically DFS with a depth cutoff
    ## limit controls how deep we are allowed to go
    ## depth here means number of moves from the start
    ## start node is depth 0

    start = find_cell(grid, "A")
    goal = find_cell(grid, "B")

    ## this set tracks the current recursion path only
    ## prevents cycling in the current route
    pathset = set()

    def recurse(current, depth_remaining):
        ## current is the current coordinate we are standing on
        ## depth_remaining is how many more steps we are allowed to take

        ## add current to the pathset to mark it as "in our current route"
        pathset.add(current)

        ## if we reached goal, we return a path containing only this node
        ## as recursion unwinds, we build the full path
        if current == goal:
            return [current]

        ## if we are out of depth, we cannot go further from here
        if depth_remaining == 0:
            pathset.remove(current)
            return None

        ## explore neighbors in DFS style (one branch at a time)
        r, c = current
        neighbors = get_neighbors(grid, r, c)

        ## we loop through neighbors and try each branch
        for neighbor in neighbors:

            ## do not revisit a cell already in the current route
            if neighbor not in pathset:

                ## recursive call reduces depth remaining by 1
                result = recurse(neighbor, depth_remaining - 1)

                ## if result is not None, that branch found the goal
                if result is not None:
                    ## return current + the successful path from deeper recursion
                    return [current] + result

        ## if no neighbor worked, remove current from pathset and backtrack
        pathset.remove(current)
        return None

    ## call recursion starting at start with the full depth limit
    found = recurse(start, limit)

    ## if found is None, DLS did not find goal within the limit
    if found is None:
        return []
    return found


def main():
    ## run DLS with limit = 4
    ## if shortest path requires more than 4 moves, this should fail (return [])
    limit4 = dls_grid_path(GRID, 4)
    print("DLS path with limit = 4:", limit4)
    if limit4:
        print("DLS path length (moves):", len(limit4) - 1)
    else:
        print("No path found within depth limit 4")

    print()

    ## run DLS with limit = 8
    ## larger limit means DLS is allowed to explore deeper
    limit8 = dls_grid_path(GRID, 8)
    print("DLS path with limit = 8:", limit8)
    if limit8:
        print("DLS path length (moves):", len(limit8) - 1)
    else:
        print("No path found within depth limit 8")


if __name__ == "__main__":
    main()
