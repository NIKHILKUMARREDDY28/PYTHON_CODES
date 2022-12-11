class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.adjMat = [[0 for i in range(self.vertices)] for j in range( self.vertices)]

    def printMatrix(self):
        for i in range(self.vertices):
            print("Adjacents of {} are\n head ".format(i),end="")
            for j in range(self.vertices):
                if self.adjMat[i][j] == 1:
                    print(" -> {}".format(j), end="")
            print()

    def add_edge(self,src,des):
        self.adjMat[src][des] = 1
        #print(self.adjMat)




if __name__ == "__main__":

    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.printMatrix()


