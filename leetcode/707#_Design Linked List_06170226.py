
# coding: utf-8

# In[1]:


class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
    
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
       
        if index<0 or index>self.len-1: return -1
        cur = self.head
        # loop backwards
        if 2*(index-1)>self.len:
            for i in range(self.len-index):
                cur = cur.prev
        # loop forward
        else:
            for i in range(index):
                cur = cur.next
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        
        if not self.head:
            self.head = Node(val)
        else:
            p = Node(val)
            if self.len == 1:
                q = self.head
            else:
                q = self.head.prev
            q.next,p.prev = p,q
            self.head.prev,p.next = p,self.head
            self.head = p
        self.len+=1

    def addAtTail(self, val: int) -> None:
        
        if not self.head:
            self.head = Node(val)
        else:
            p = Node(val)
            if self.len == 1:
                q = self.head
            else:
                q = self.head.prev
            q.next,p.prev = p,q
            p.next,self.head.prev = self.head,p
        self.len+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index<0 or index>self.len: return
        if index == self.len: self.addAtTail(val)
        elif not index: self.addAtHead(val)
        else:
            cur = self.head
            # loop backwards
            if 2*(index-1)>self.len:
                for i in range(self.len-index):
                    cur = cur.prev
            # loop forward
            else:
                for i in range(index):
                    cur = cur.next
            p = Node(val)
            q = cur.prev
            q.next,p.prev = p,q
            p.next,cur.prev = cur,p
            self.len+=1
             
        
    def deleteAtIndex(self, index: int) -> None:
   
        if index<0 or index>self.len-1: return
        elif self.len==1:
            self.head,self.len = None,0     
        else:
            cur = self.head
            if 2*(index-1)>self.len:
                for i in range(self.len-index):
                    cur = cur.prev
            else:
                for i in range(index):
                    cur = cur.next
            p = cur.prev
            q = cur.next
            p.next,q.prev = q,p
            self.len-=1

