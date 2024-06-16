class Graph:
    def __init__(self):
        self.adjecency_list = {}
    def add_edge(self,vertex1,vertex2):
        if vertex1 not in self.adjecency_list:
             self.adjecency_list[vertex1] = []
        if vertex2 not in self.adjecency_list:
            self.adjecency_list[vertex2] = []
        self.adjecency_list[vertex1].append(vertex2)
        self.adjecency_list[vertex2].append(vertex1)
    def remove_edge(self,vertex1,vertex2):
        if vertex1 in self.adjecency_list and vertex2 in self.adjecency_list:
            self.adjecency_list[vertex1].remove(vertex2)
            self.adjecency_list[vertex2].remove(vertex1)
    def display(self):
        for vertex,edge in self.adjecency_list.items():
            print(f"{vertex}:{edge}")
    def bfs(self,start_vertex):
        visited = set()
        queue = [start_vertex]
        while queue:
            curent_vertex = queue.pop(0)
            if curent_vertex not in visited:
                print(curent_vertex,' ',end="")
                visited.add(curent_vertex)
                queue.extend(self.adjecency_list[curent_vertex])
        print()
    def dfs(self,start_vertex):
        visited = set()
        def dfs_recurse(vertex):
            if vertex not in visited:
                print(vertex,' ',end="")
                visited.add(vertex)
                for neighbor in self.adjecency_list[vertex]:
                    dfs_recurse(neighbor)
        dfs_recurse(start_vertex)
           

grap = Graph()
grap.add_edge(1,2)
grap.add_edge(1,3)
grap.add_edge(2,3)
grap.add_edge(3,4)
grap.bfs(2)
grap.display()
grap.dfs(2)


