from labyrinth import Labyrinth

def DFS(lab:Labyrinth):
    print('Starting DFS')
    trail = []

    #TODO

    return trail

def BFS(lab:Labyrinth):
    print('Starting BFS')
    trail = []
    visited = {}
    final = False
    
    sc = lab.getStartCell()
    ec = lab.getEndCell()
    c = sc
    toVisit = []

    # 1. getChildren
    # 2. comprovar que cap és EndCell
    # 3. toVisit.append
    
    while not final:
        for y in c.getChildren(): # per totes les caselles conectades a c
            if y not in visited and y != ec: # si la visitem per primer cop i no és la EndCell
                toVisit.append(y) # la afegim per visitar
                visited[y]="0" # 
            elif y == ec:
                final = True
                print(y)
            
        c = toVisit.pop()

    return trail

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
