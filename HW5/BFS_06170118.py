from collections import defaultdict 

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        queue = []
        final = []
        final.append(s)
        queue = queue+self.graph[s]
        while len(queue) != len(final)-1:
            for i in queue:
                if i in final:
                    continue
                final.append(i)
                for n in self.graph[i]:
                    if n not in queue:
                        if n not in final:
                            queue.append(n)
                break
        return final
    def DFS(self, s):
        stack = []
        final = []
        final.append(s)
        stack = stack+self.graph[s]
        while len(stack) != len(final)-1:
            for i in reversed(stack):
                if i in final:
                    continue
                final.append(i)
                for n in self.graph[i]:
                    if n not in stack:
                        if n not in final:
                            stack.append(n)
                break
        return final
     
#參考資料: https://seanlhlee.gitbooks.io/acosa/gitBook/Data%20Structures/Graphs/breadth-first_search.html
#          https://seanlhlee.gitbooks.io/acosa/gitBook/Data%20Structures/Graphs/depth-first_search.html
#          https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/102866/#outline__1_1_3
