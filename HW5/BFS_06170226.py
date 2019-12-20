
# coding: utf-8

# In[18]:


from collections import defaultdict 
  

class Graph:
   
    def __init__(self): 
        self.graph = defaultdict(list) 
    
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
   
    def BFS(self, s): 
        s2 = [] 
        queue = [s]
      
        
        while queue:
            s = queue.pop(0)
            s2.append(s)
            for child in self.graph[s]:
                if child not in s2:
                    queue.append(child)
        
        return s2
    
    def DFS(self, s): 
        s2 = [] 
        stack = [s]
        
        while stack:
            s=stack.pop(-1)
            s2.append(s)
            for child in self.graph[s]:
                if child not in s2:
                    stack.append(child)
                    
        return s2


# In[24]:






# In[23]:




