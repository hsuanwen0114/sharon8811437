```class Nodes:
    def __init__(self,data=None):
        self.prev = None
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = Nodes()

    def insertBack(self,data):
        newNode = Nodes(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode
        newNode.prev = cur

    def insertFront(self,data):   
        newNode = Nodes(data)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode 
        
    def printList(self):
        cur = self.head
        arr = []
        while cur: 
            if cur.data != None:
                arr.append(cur.data)
            cur = cur.next
        print(arr)

    def remove(self,gone):
        cur = self.head
        print("-------",gone,"will be gone -----")
        while cur:
            if cur.data == gone:
                cur.prev.next = cur.next    
            cur = cur.next

    def reverseOrder(self):
        print("  <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        cur = self.head
        lastOne = None
        nextOne = None
        cur = cur.next
        while cur:
            nextOne = cur.next
            cur.next = lastOne
            lastOne = cur
            cur = nextOne
        self.head = lastOne
```        
一開始因為ＢＳＴ所以打了linkedlist的程式碼，首先要了解他的意思：  
連結串列(Linked List)是串列(List)的一種，是一種常見的資料結構，利用這個資料結構也能進一步實作出其他的資料結構，例如堆疊(Stack)和佇列(Queue)等。  
它的特性是能夠不使用連續的記憶體空間的情況下，能夠保有並使用一份連續的資料；相對來看，陣列則需要使用連續的記憶體空間。  
流程圖如下（擷取網路上）  
![](https://medium.com/@tobby168/%E7%94%A8python%E5%AF%A6%E4%BD%9Clinked-list-524441133d4d)
