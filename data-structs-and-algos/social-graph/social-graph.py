# Given a social graph and two users as input, write a function
# to return the smallest number of friendship between the two users.

# Example: (A, B),(A, C),(B, D),(D, E) input: A, E return: 3

from graphs import Graph, Vertex

def least_friends(v1, v2):
    pass


def main():
    graph = Graph()
    val = 0
    while val != 'stop':
        val = input()
        if val == 'stop':
            break

        val = val.split()
        if val[0] == 'add':
            graph.add_vertex(val[1])

        if val[0] == 'edges':
            graph.add_edge(val[1], val[2], 0)
    
    print(graph.get_vertices())


if __name__ == '__main__':
    main()