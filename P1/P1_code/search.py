from labyrinth import Labyrinth

def rec_DFS(current_cell, visited, endcell):
    '''
    Pre-condition: current_cell siendo la celda cuyos hijos queremos visitar, visited la lista de celdas visitadas y endcell la salida del laberinto
    Post-condition: current_cell si current_cell == endcell, [] si no hay camino posible, o una lista de las celdas devueltas, que resultaran ser el camino una vez se retorne a DFS()
    '''
    # we make sure that the actual cell isn't the final one. If it is, we return it directly.
    if current_cell == endcell:
        return [current_cell]
    else:
        # loop that treats current_cell's childs
        for child in current_cell.getChildren():
            # if the child was not visited before child
            if child not in visited:
                # we mark him as visited
                visited[child]=0
                # we save the return value from the child's recursive function
                ret = rec_DFS(child, visited, endcell)
                # we make sure that the lenght of the value from the recursive function is > 0
                if len(ret) > 0:
                    # if it is, it means that the function didn't return the empty list, wich means that it didn't find the exit
                    return list([current_cell] + ret)
                # if it's not, it means that the function returned the empty list and it didn't find any path, so we proceed to do the next iteration
    # if it reaches this point means that there is'nt any possible path to reach the end
    return []
                
def DFS(lab:Labyrinth):
    print('Starting DFS')

    start = lab.getStartCell()
    end = lab.getEndCell()
    visited = {start: 0}

    return rec_DFS(start, visited, end)

def BFS(lab:Labyrinth):
    '''
    Pre-condition: Que Labyrinth sea un laberinto de tipo lab.
    Post-condition: BFS(lab:Labyrinth) = al path més curt de S a E
    '''
    print('Starting BFS')
    end = lab.getEndCell()
    # we create a dicctionary to keep track of the visited cells
    visited = {}
    # we create a list saving the possible paths
    possible_paths = [[lab.getStartCell()]]

    # loop while there are paths to check
    while possible_paths:
        # we try a possible path
        path = possible_paths.pop(0)
        # in the last cell from the possible path to search for children
        current_cell = path[-1]
        # if the current cell hasn't been visited
        if current_cell not in visited:
            # we check pne by one current cell's children
            for child in current_cell.getChildren():
                # we create a new possible path formed by: father's path + this child
                new_possible_path = list(path)
                new_possible_path.append(child)
                # if the child is the exit, we return the new (possible) path, that it has turned out to be the solution
                if child == end:
                    return new_possible_path
                # if not, we add it to the possible paths list
                possible_paths.append(new_possible_path)
    
            # we add the current cell to the visited cells list
            visited[current_cell]=0
    # if we reach this point, it means that there is no possible path, so we return an empty list
    return []

if __name__ == '__main__':
    algo_choices = ['BFS', 'DFS']
    algo_funcs = [BFS, DFS]

    import argparse
    argp = argparse.ArgumentParser()
    argp.add_argument('labyrinth_file')
    argp.add_argument('algo', choices=algo_choices)

    args = argp.parse_args()
    laby = Labyrinth.load_from_file(args.labyrinth_file)
    print(laby)
    result_trail = algo_funcs[algo_choices.index(args.algo)](laby)
    if result_trail:
        print(f'{args.algo} found solution that has {len(result_trail)} steps:')
        print(result_trail)
