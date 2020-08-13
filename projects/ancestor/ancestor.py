

# Plan
'''
1.  Build graph with the ancestor and (parent, child) pairs
2.  Perform DFS on given starting node
'''

def earliest_ancestor(ancestors, starting_node):

    #build graph
    vertices = {}

    for pair in ancestors:
        v = pair[1]

        if v not in vertices:
            vertices[v] = set()

        vertices[v].add(pair[0])
    
    paths = []

    #search graph depth-first
    def dfs_search(path, visited=set()):
        current_v = path[-1]
        
        if current_v not in vertices:
            paths.append(path)
        else:
            children = vertices[current_v]  
            for v in children:
                if v not in visited:
                    visited.add(v)
                    new_path = list(path)
                    new_path.append(v)
                    dfs_search(new_path, visited)

    dfs_search([starting_node])

    
    max_len_index = 0
    for i in range(1, len(paths)):
        if len(paths[i]) > len(paths[max_len_index]):
            max_len_index = i
        elif len(paths[i]) == len(paths[max_len_index]):
            if paths[i][-1] < paths[max_len_index][-1]:
                max_len_index = i

    if len(paths[max_len_index]) > 1:
        return paths[max_len_index][-1]
    
    return -1
        









test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1)) #10    
print(earliest_ancestor(test_ancestors, 2)) #-1
print(earliest_ancestor(test_ancestors, 3)) #10

