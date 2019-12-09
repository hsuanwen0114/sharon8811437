
# coding: utf-8

# In[125]:


from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self,key):
        a = MD5.new()
        a.update(key.encode("utf-8"))
        key = int(a.hexdigest(),16)
        index = key % self.capacity
        n = self.data[index]
        
        
        if self.data[index] == None:
            self.data[index] = ListNode(key)
         
           
            
            
        else:    
            while n.next is not None:
                n = n.next
                
            n.next = ListNode(key)
          
            
        
            
    def remove(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        x = h.hexdigest()
        key = int(h.hexdigest(),16)
        index = key % self.capacity
        node = self.data[index]
        
        if node.val == key:
            if node.next == None:
                self.data[index] = None
            else:
                self.data[index] = node.next
                
                return 
        else:
            node = self.data[index]
            o = None
            while node.next.val is not key:
                o = node
                node = node.next
            if node.val == key:
                o.next=node.next
        return
           
            
    
    def contains(self, key):
        a = MD5.new()
        a.update(key.encode("utf-8"))
        key = int(a.hexdigest(),16)
        index = key % self.capacity
        n = self.data[index]
        
        if self.data[index]==None:
            return False
        
        else:
            node=self.data[index]
            while node is not None:
                if node.val == key:
                    return True
                else:
                    node=node.next
                    
        return False
                    
        


# In[126]:


hashSet = MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel = hashSet.contains("pig")
print(rel)
rel = hashSet.contains("dog")
print(rel)
rel = hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel = hashSet.contains("bird")
print(rel)
hashSet.add("pig")
hashSet.remove("pig")
rel = hashSet.contains("pig")
print(rel)

