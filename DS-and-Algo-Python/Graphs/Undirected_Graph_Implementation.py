class Graph:
    
    def __init__(self):
        self.number_of_nodes=0
        self.adjacency_list={}
    
    def addVertex(self,data):
        self.adjacency_list[data]=[]
        self.number_of_nodes+=1
    
    def addEdge(self,vertex1,vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)
        
    def showconnection(self):
        for x in self.adjacency_list:
            print(x,end='->')
            for i in self.adjacency_list[x]:
                print(i,end=' ')
            print()

my_graph = Graph()
my_graph.addVertex(1)
my_graph.addVertex(2)
my_graph.addVertex(3)
my_graph.addEdge(1,2)
my_graph.addEdge(1,3)
my_graph.addEdge(2,3)
print(my_graph.adjacency_list)
#{1: [2, 3], 2: [1, 3], 3: [1, 2]}
my_graph.showconnection()
'''
1->2 3 
2->1 3 
3->1 2 
'''
print(my_graph.number_of_nodes)