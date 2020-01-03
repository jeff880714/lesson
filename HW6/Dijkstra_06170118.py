from collections import defaultdict 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.dict = defaultdict(list) 
    def addEdge(self,u,v,w): 
        self.dict[w].append([u,v])
    def Dijkstra(self, s): 
        test = [False] * self.V 
        dist = [float('inf')] * self.V
        
        dist[s] = 0
        
        while test != [True] * self.V:
            for i in range(self.V):
                if g.graph[s][i] != 0 and dist[s] + g.graph[s][i] < dist[i]:
                    dist[i] = dist[s] + g.graph[s][i]
                           
            m = float('inf')
            for k in range(self.V):
                if test[k] == False and dist[k] < m :
                    m = dist[k]
                    s = k         
            test[s] = True
            
            diction = {} 
            if test == [True] * self.V:
                for i in range(self.V):
                    diction[str(i)] = dist [i]
                return diction
        return answer
    def Kruskal(self):
        answer={}
        check = [column for column in range(self.V)]  
        val = sorted(self.dict)
        for i in val:
            for f,s in self.dict[i]:
                if check[f] == check[s]:
                    pass
                else:
                    check = [check[f] if x==check[s] else x for x in check]
                    answer[str(f)+'-'+str(s)] = i
        return answer
#參考資料:https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
#        https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
#        http://dreamisadream97.pixnet.net/blog/post/168577620-dijkstra%E6%BC%94%E7%AE%97%E6%B3%95
#        https://sites.google.com/site/zsgititit/home/jin-jiec-cheng-shi-she-ji-2/zui-xiao-sheng-cheng-shu
