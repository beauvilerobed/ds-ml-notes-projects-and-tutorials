# Given a social graph and two users as input, write a function
# to return the smallest number of friendship between the two users.

# Example: (A, B),(A, C),(B, D),(D, E) input: A, E return: 3

# solution: runtime O(N*M) N number of users, M number of friendships space complexity O(N)

from graphs import Graph, Vertex

def least_friends(graph, v1, v2):
    n = len(graph.vertices)
    visited = [False]*(n+1)
    counts = [0]*(n+1)
    queue = []
    queue.append(v1)

    while queue:
        curr = queue.pop(0)
        for i in graph.get_vertex(curr).get_neighbors():
            if visited[i.val] == False:
                counts[i.val] = counts[curr] + 1
                queue.append(i.val)
                visited[i.val] = True
    return counts[v2]

def main():
    graph = Graph()
    val = 0
    inputs = ["add 1", "add 2", "add 3", "add 4", "add 5", "edges 1 2", "edges 1 3", "edges 2 4", "edges 4 5"]
    n = len(inputs)
    for input in inputs:
        val = input.split()
        if val[0] == 'add':
            graph.add_vertex(int(val[1]))

        if val[0] == 'edges':
            graph.add_edge(int(val[1]), int(val[2]), 0)
    
    print(graph.get_vertices())
    print(graph.get_vertex(1).get_neighbors())
    print(least_friends(graph, 1, 5))


if __name__ == '__main__':
    main()