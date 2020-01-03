
# coding: utf-8

# In[14]:


from collections import defaultdict

#Class to represent a graph
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]
                    for row in range(vertices)]
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def Dijkstra(self, s):

        havevisit = []
        distance = {s: 0}
        node = list(range(self.V))
        if s in node:
            node.remove(s)
            havevisit.append(s)
        else:
            return None

        for d in node:
            distance[d] = self.graph[s][d]
        pick = s
        while node:
            _distance = float('inf')
            for d in havevisit:
                for e in node:
                    if self.graph[d][e] > 0:
                        if _distance > distance[d] + self.graph[d][e]:
                            _distance = distance[e] = distance[d] + self.graph[d][e]
                            pick = e
            havevisit.append(pick)
            node.remove(pick)

        aaa = {}
        for i in range(self.V):
            aaa[str(i)] = distance[i]
        return aaa

    def find(self, x, pres):
        root, p = x, x
        while root != pres[root]:
            root = pres[root]

        while p != pres[p]:
            p, pres[p] = pres[p], root
        return root

    def find(self, z, press):
        root, b = z, z
        while root != press[root]:
            root = press[root]

        while b != press[b]:
            b, press[b] = press[b], root
        return root

    def join(self, z, q, press, front):
        c1, c2 = self.find(z, press), self.find(q, press)
        if c1 is not c2:
            if front[c1] < front[c2]:
                press[c1] = c2
            else:
                press[c2] = c1
                if front[c1] == front[c2]:
                    front[c1] += 1
                    
    def Kruskal(self):
        a = self.V
        p, front = [e for e in range(a)], [0] * a
        edges = sorted(self.graph, key=lambda x: x[-1])
        mst_edges, num = [], 0
        for edge in edges:
            if self.find(edge[0], p) is not self.find(edge[1], p):
                mst_edges.append(edge)
                self.join(edge[0], edge[1], p, front)
                num += 1
            else:
                continue
            if num == a:
                break
        aaa = {}
        for [u, v, w] in mst_edges:
            aaa[str(u)+'-'+str(v)] = w
        return aaa


#參考資料：老師上課、ppt、同學程式碼
