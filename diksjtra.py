from collections import defaultdict

class Node_Distance :

    def __init__(self, name, dist) :
        self.name = name
        self.dist = dist

class Graph :

    def __init__(self, node_count) :
        self.adjlist = defaultdict(list)
        self.node_count = node_count

    def Add_Into_Adjlist(self, src, node_dist) :
        self.adjlist[src].append(node_dist)

    def Dijkstras_Shortest_Path(self, source) :
        distance = [999999999999] * self.node_count
        distance[source] = 0
        dict_node_length = {source: 0}

        while dict_node_length :
            current_source_node = min(dict_node_length, key = lambda k: dict_node_length[k])
            del dict_node_length[current_source_node]

            for node_dist in self.adjlist[current_source_node] :
                adjnode = node_dist.name
                length_to_adjnode = node_dist.dist
                if distance[adjnode] > distance[current_source_node] + length_to_adjnode :
                    distance[adjnode] = distance[current_source_node] + length_to_adjnode
                    dict_node_length[adjnode] = distance[adjnode]

        for i in range(self.node_count) :
            print("Source Node ("+str(source)+")  -> Destination Node(" + str(i) + ")  : " + str(distance[i]))

def main() :

    g = Graph(6)

    # Node 0: <1,5> <2,1> <3,4>
    g.Add_Into_Adjlist(0, Node_Distance(1, 5))
    g.Add_Into_Adjlist(0, Node_Distance(2, 1))
    g.Add_Into_Adjlist(0, Node_Distance(3, 4))

    # Node 1: <0,5> <2,3> <4,8> 
    g.Add_Into_Adjlist(1, Node_Distance(0, 5))
    g.Add_Into_Adjlist(1, Node_Distance(2, 3))
    g.Add_Into_Adjlist(1, Node_Distance(4, 8))

    # Node 2: <0,1> <1,3> <3,2> <4,1>
    g.Add_Into_Adjlist(2, Node_Distance(0, 1))
    g.Add_Into_Adjlist(2, Node_Distance(1, 3))
    g.Add_Into_Adjlist(2, Node_Distance(3, 2))
    g.Add_Into_Adjlist(2, Node_Distance(4, 1))

    # Node 3: <0,4> <2,2> <4,2> <5,1>
    g.Add_Into_Adjlist(3, Node_Distance(0, 4))
    g.Add_Into_Adjlist(3, Node_Distance(2, 2))
    g.Add_Into_Adjlist(3, Node_Distance(4, 2))
    g.Add_Into_Adjlist(3, Node_Distance(5, 1))

    # Node 4: <1,8> <2,1> <3,2> <5,3>
    g.Add_Into_Adjlist(4, Node_Distance(1, 8))
    g.Add_Into_Adjlist(4, Node_Distance(2, 1))
    g.Add_Into_Adjlist(4, Node_Distance(3, 2))
    g.Add_Into_Adjlist(4, Node_Distance(5, 3))

    # Node 5: <3,1> <4,3> 
    g.Add_Into_Adjlist(5, Node_Distance(3, 1))
    g.Add_Into_Adjlist(5, Node_Distance(4, 3))

    g.Dijkstras_Shortest_Path(0)
    print("\n")
    g.Dijkstras_Shortest_Path(5)

if __name__ == "__main__" :
   main()

