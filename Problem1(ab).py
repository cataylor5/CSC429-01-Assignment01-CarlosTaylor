from collections import deque

# graph for problems a, b
## quotes node A contains : the set of nodes [] seperated by commas
GRAPH = {
    "A": ["B"],  ##goes from a to b
    "B": ["C", "D"],  ##goes to btoh c and d
    "C": ["E"],
    "D": ["F"],
    "E": [],  ## must include even though e is leaf
    "F": [],
}


def bfs_path(adj, start, goal):
    ##variable name(frontier) = name of list to hold explored nodes
    ## (deque) is a tool in the collections toolbox; a list designed to add items, remove, especially from front
    ##(([start])) square brackets create a list. 'start' refers to the fucntion parameter's variable for the first node
    frontier = deque([start])

    ## parent is a marker variable for the node that precedes the current one. it allows us to reconstruct our pathtaken
    ##the parent of start is None, because it is the first node in the BFS
    ##{} curly braces create a dictionary of key value pairs "this : is paired with this"
    ## None is a special value meaining. it means nothing. nothing else.
    parent = {start: None}

    ##this is similar to the above, but it is not a dictionary, it is a set. because there are no paired values
    explored = {start}

    ## while the frontier still has nodes to explore
    ## in python, "while frontier:" means "while the list is not empty"
    while frontier:

        ## popleft removes and returns the first element in the deque
        ## this is what makes BFS breadth-first (first in, first out)
        current = frontier.popleft()

        ## if we have reached our goal node, we stop searching
        if current == goal:

            ## we now reconstruct the pathtaken by walking backward using parent
            ## we start at the goal and trace back to the start
            pathtaken = []
            node = goal

            ## while node is not None (None marks the beginning)
            while node is not None:

                ## append current node to pathtaken list
                pathtaken.append(node)

                ## move backward to its parent
                node = parent[node]

            ## pathtaken is currently reversed (goal to start), so reverse it
            pathtaken.reverse()

            ## return the completed pathtaken
            return pathtaken

        ## if we did not hit the goal yet, we explore neighbors

        ## adj.get(current, []) safely returns neighbor list for 'current' node
        ## neighbor creates temporary variable to represent each connected node at a time
        for neighbor in adj.get(current, []):

            ## only process neighbor if we have not already explored it
            if neighbor not in explored:

                ## mark neighbor as explored immediately
                explored.add(neighbor)

                ## record how we reached this neighbor
                ## this is how we later reconstruct the pathtaken
                parent[neighbor] = current

                ## add neighbor value to the frontier queue to explore later
                frontier.append(neighbor)

    ## if we exit the while loop without finding goal,
    ## that means there is no path
    return []


def dfs_path(adj, start, goal):

    ## DFS uses a stack instead of a queue
    ## instead of first in first out (FIFO), it is last in first out (LIFO)
    ## we begin by placing the start node into the stack (frontier)
    frontier = [start]

    ## parent dictionary serves same purpose as in BFS
    ## it stores the node that precedes the current node
    ## start has no parent because it is the first node
    parent = {start: None}

    ## explored is a set to prevent revisiting nodes
    ## we immediately mark start as explored
    explored = {start}

    ## while there are still nodes in the frontier (stack)
    while frontier:

        ## pop removes and returns the last item in the list
        ## this is what makes DFS depth first (goes down one branch fully before backtracking)
        current = frontier.pop()

        ## if we have reached the goal node, reconstruct the pathtaken
        if current == goal:

            ## create empty list to store pathtaken
            pathtaken = []
            node = goal

            ## trace backward from goal to start using parent dictionary
            while node is not None:

                ## add current node to pathtaken
                pathtaken.append(node)

                ## move backward to the parent node
                node = parent[node]

            ## pathtaken is reversed (goal to start), so reverse it
            pathtaken.reverse()

            ## return completed pathtaken
            return pathtaken

        ## if goal not yet reached, explore neighbors

        ## retrieve list of neighbors connected to current node
        ## adj.get ensures we do not cause error if node not found
        neighbors = adj.get(current, [])

        ## reversed is used so that leftmost neighbor is explored first
        ## because stack pops last added item first
        for neighbor in reversed(neighbors):

            ## only proceed if neighbor has not already been explored
            if neighbor not in explored:

                ## mark neighbor as explored
                explored.add(neighbor)

                ## record how we reached neighbor
                parent[neighbor] = current

                ## add neighbor to frontier stack to explore next
                frontier.append(neighbor)

    ## if stack empties without reaching goal, no path exists
    return []


## we define a function 'main' that takes no arguments
def main():
    ## Part (a) BFS from A to E
    bfs_result = bfs_path(GRAPH, "A", "E")
    print("BFS path from A to E:", bfs_result)

    ## Part (b) DFS from A to E
    dfs_result = dfs_path(GRAPH, "A", "E")
    print("DFS path from A to E:", dfs_result)


## If the special built-in variable __name__ equals the string "__main__", then execute the following block
if __name__ == "__main__":
    main()
