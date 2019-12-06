
# coding: utf-8

# In[91]:


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
            return
            
        else:    
            node = ListNode(key)
            while node.next is not None:
                node = node.next
                
            node.next = LinkNode(key)
            
    def remove(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        x = h.hexdigest()
        key = int(h.hexdigest(),16)
        index = key % self.capacity
        node = self.data[index]
        
        if node == key and node.val == key:
            self.data[index] = node.next
            return 
        
        else:
            node = self.data[index]
            while node.next:
                if node.next.val == [index]:
                    node.next = node.next.next
                    return 
                node.next = node.next.next
            else:
                return False           
            
    
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
                    
        


# In[92]:


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
hashSet.remove("pig")
rel = hashSet.remove("bird")
print(rel)

