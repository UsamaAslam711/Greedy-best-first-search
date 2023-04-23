from sys import flags


# graph = {
#     'A': [[3, 'B'], [4, 'D'], [5, 'E']],
#     'B': [[1, 'C']],
#     'C': [[3, 'I'], [1, 'G']],
#     'D': [[2, 'F']],
#     'E': [[2, 'C'], [1, 'I']],
#     'F': [[1, 'E'], [2, 'H']],
#     'G': [],
#     'H': [[1, 'I']],
#     'I': [[5, 'G']],
# }
# ------------------------------------------------------------------------------------
# graph = {
#     'S': [[5, 'A'], [9, 'B'], [6, 'D']],
#     'A': [[3, 'B'], [9, 'G1']],
#     'B': [[1, 'C'], [2, 'A']],
#     'C': [[6, 'S'], [5, 'G2'], [7, 'F']],
#     'D': [[1, 'S'], [2, 'C'], [2, 'E']],
#     'E': [[7, 'G3']],
#     'F': [[2, 'D'], [8, 'G3']],
#     'G1': [],
#     'G2': [],
#     'G3': []
# }
# ------------------------------------------------------------------------------------

# graph = {
#     'Arad': [[75, 'Zerind'], [118, 'Timisoara'], [140, 'Sibiu']],
#     'Zerind': [[71, 'Oradea']],
#     'Oradea': [[151, 'Sibiu']],
#     'Timisoara': [[111, 'Lugoj']],
#     'Lugoj': [[70, 'Mehadia']],
#     'Mehadia': [[75, 'Drobeta']],
#     'Drobeta': [[120, 'Craiova']],
#     'Craiova': [[138, 'Pitesti'], [146, 'Rimnicu Vilcea']],
#     'Sibiu': [[99, 'Fagaras'], [80, 'Rimnicu Vilcea']],
#     'Rimnicu Vilcea': [[97, 'Pitesti']],
#     'Fagaras': [[211, 'Bucharest']],
#     'Pitesti': [[101, 'Bucharest']],
#     'Bucharest': [[90, 'Giurgiu'], [85, 'Urziceni']],
#     'Urziceni': [[98, 'Hirsova'], [142, 'Vaslui']],
#     'Hirsova': [[86, 'Eforie']],
#     'Vaslui': [[92, 'Iasi']],
#     'Iasi': [[87, 'Neamt']],
#     'Giurgiu': [],
#     'Neamt': [],
#     'Eforie': [],
# }
# ------------------------------------------------------------------------------------

graph = {
    'S': [[10.4, 3,'A'], [8.9, 4,'D']],
    'A': [[6.7, 4,'B'], [8.9, 5,'D']],
    'B': [[4.0, 4,'C']],
    'C': [],
    'D': [[6.9, 2, 'E']],
    'E': [[3.0, 4, 'F']],
    'F': [[0, 3, 'G']],
    'G': [],
}


def a_star(graph, node, goal):  # function for BFS
    visited = []  # List for visited nodes.
    queue = []  # Initialize a queue
    cost = 0
    flag = False

    queue.append([0, 0, node])

    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        visited.append(m[2])
        if m[2] == goal:
            print(m[2], '\tGoal Acheived !!!')
            return

        cost = m[1]
        print(m[2])
        for neighbour in graph[m[2]]:
            flag = False
            if neighbour[2] == 'E':
                print('\n')
            if neighbour[2] not in visited:
                for arr in queue:  # Agar queue me already aik key pari hwi hai to uski cost ko update krne k liye
                    if arr[2] == neighbour[2]:
                        # Agar already pari hwi key ki value pehlye hi choti hai ab wali value se to change na karo
                        if arr[0] > neighbour[0]+cost:
                            arr[0] = neighbour[0]+cost
                        flag = True

                if flag != True:
                    queue.append([neighbour[1]+cost+neighbour[0], neighbour[1]+cost, neighbour[2]])

        queue.sort()
        

# Driver Code
print("Following is the Breadth-First Search")
a_star(graph, 'S', 'G') 