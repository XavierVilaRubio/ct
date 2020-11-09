from labyrinth import Labyrinth

def rec_DFS(current_cell, visited, endcell):
    # comprovem que la cell actual no sigui la final, si ho és directament la tornem
    if current_cell == endcell:
        return [current_cell]
    else:
        # bucle per tractar els fills de current_cell
        for child in current_cell.getChildren():
            # si encara no hem visitat el child
            if child not in visited:
                # el marquem com a visitat
                visited[child]=0
                # preparem el valor de retorn format per la current_cell + la funció recursiva del fill
                ret = list([current_cell] + rec_DFS(child, visited, endcell))
                # si l'ultima posició no és la endcell significa que no ha aconseguit arribar al final
                if ret[-1] != endcell:
                    # per tant anem a la següent iteració del for
                    continue
                # si l'última posició sí que és la endcell significa que ha arribat a la sortida del laberint
                else:
                    # retornem la current_cell + la funció recursiva del fill
                    return ret
    # si arriba aquí significa que no ha trobat cap path possible
    return []
                
def DFS(lab:Labyrinth):
    print('Starting DFS')

    start = lab.getStartCell()
    end = lab.getEndCell()
    visited = {start: 0}

    return rec_DFS(start, visited, end)

def BFS(lab:Labyrinth):
    print('Starting BFS')
    end = lab.getEndCell()
    # we create a dicctionary to keep track of the visited cells
    visited = {}
    # creem una llista per anar guardant els possibles paths
    possible_paths = [[lab.getStartCell()]]

    # bucle mentres encara quedin paths per comprovar
    while possible_paths:
        # agafem una possible ruta
        path = possible_paths.pop(0)
        # agafem l'última cell del possible path, per continuar mirant els seus childrens
        current_cell = path[-1]
        # si la current_cell encara no ha estat visitatda
        if current_cell not in visited:
            # tractem un per un tots els children de current_cell
            for child in current_cell.getChildren():
                # creem un nou possible path format per: el path del pare + aquest child
                new_possible_path = list(path)
                new_possible_path.append(child)
                # si el child és el final, retornem el nou (possible) path, que ha resultat ser la solució
                if child == end:
                    return new_possible_path
                # si no, l'afegim a la llista de possibles paths
                possible_paths.append(new_possible_path)
    
            # afegin la current_cell a la llista de visitades
            visited[current_cell]=0
    # si arriba aquí significa que no ha trobat cap path, per tant retornem una llista buida
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
